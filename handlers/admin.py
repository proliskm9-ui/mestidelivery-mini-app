from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from config import ADMIN_IDS
from database import (
    get_stats,
    get_language_stats,
    get_users_by_audience,
    count_users_by_audience,
    mark_user_blocked,
    get_user_language,
)
from keyboards import (
    admin_keyboard,
    broadcast_audience_keyboard,
    broadcast_confirm_keyboard,
    main_keyboard,
)
from texts import t
from admin_texts import (
    admin_panel_text,
    admin_stats_text,
    broadcast_choose_audience_text,
    broadcast_waiting_text,
    broadcast_confirm_text,
    broadcast_done_text,
    broadcast_started_text,
    broadcast_cancelled_text,
)

router = Router()


class BroadcastState(StatesGroup):
    waiting_message = State()
    confirm = State()


def is_admin(user_id: int) -> bool:
    return user_id in ADMIN_IDS


@router.message(Command('admin'))
async def cmd_admin(message: Message, state: FSMContext):
    if not is_admin(message.from_user.id):
        return
    await state.clear()
    await message.answer(admin_panel_text(), reply_markup=admin_keyboard())


@router.callback_query(F.data == 'admin_menu')
async def admin_menu(callback: CallbackQuery, state: FSMContext):
    if not is_admin(callback.from_user.id):
        return await callback.answer('Нет доступа', show_alert=True)
    await state.clear()
    await callback.message.edit_text(admin_panel_text(), reply_markup=admin_keyboard())
    await callback.answer()


@router.callback_query(F.data == 'admin_stats')
async def admin_stats(callback: CallbackQuery):
    if not is_admin(callback.from_user.id):
        return await callback.answer('Нет доступа', show_alert=True)

    stats = await get_stats()
    lang_stats = await get_language_stats()
    await callback.message.edit_text(
        admin_stats_text(stats, lang_stats),
        reply_markup=admin_keyboard(),
    )
    await callback.answer()


@router.callback_query(F.data == 'admin_broadcast')
async def admin_broadcast(callback: CallbackQuery, state: FSMContext):
    if not is_admin(callback.from_user.id):
        return await callback.answer('Нет доступа', show_alert=True)

    await state.clear()
    await callback.message.edit_text(
        broadcast_choose_audience_text(),
        reply_markup=broadcast_audience_keyboard(),
    )
    await callback.answer()


@router.callback_query(F.data.startswith('broadcast_aud_'))
async def broadcast_audience_selected(callback: CallbackQuery, state: FSMContext):
    if not is_admin(callback.from_user.id):
        return await callback.answer('Нет доступа', show_alert=True)

    audience = callback.data.removeprefix('broadcast_aud_')
    recipients = await count_users_by_audience(audience)

    if recipients == 0:
        return await callback.answer(
            'В этой аудитории пока нет пользователей',
            show_alert=True,
        )

    await state.update_data(audience=audience, recipients=recipients)
    await state.set_state(BroadcastState.waiting_message)
    await callback.message.edit_text(
        broadcast_waiting_text(audience, recipients),
        reply_markup=broadcast_audience_keyboard(),
    )
    await callback.answer()


@router.message(BroadcastState.waiting_message)
async def broadcast_message_received(message: Message, state: FSMContext):
    if not is_admin(message.from_user.id):
        return

    data = await state.get_data()
    audience = data.get('audience', 'all')
    recipients = data.get('recipients', 0)

    await state.update_data(
        message_id=message.message_id,
        chat_id=message.chat.id,
    )
    await state.set_state(BroadcastState.confirm)
    await message.answer(
        broadcast_confirm_text(audience, recipients),
        reply_markup=broadcast_confirm_keyboard(),
    )


@router.callback_query(F.data == 'broadcast_confirm', BroadcastState.confirm)
async def broadcast_confirm(callback: CallbackQuery, state: FSMContext):
    if not is_admin(callback.from_user.id):
        return

    data = await state.get_data()
    audience = data.get('audience', 'all')
    users = await get_users_by_audience(audience)

    await callback.message.edit_text(broadcast_started_text())

    success, failed = 0, 0
    for user in users:
        try:
            await callback.bot.copy_message(
                chat_id=user.id,
                from_chat_id=data['chat_id'],
                message_id=data['message_id'],
            )
            success += 1
        except Exception:
            failed += 1
            await mark_user_blocked(user.id)

    await state.clear()
    await callback.message.edit_text(
        broadcast_done_text(audience, success, failed),
        reply_markup=admin_keyboard(),
    )


@router.callback_query(F.data == 'broadcast_cancel', BroadcastState.confirm)
async def broadcast_cancel(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    await callback.message.edit_text(broadcast_cancelled_text(), reply_markup=admin_keyboard())
    await callback.answer()


@router.callback_query(F.data == 'admin_back')
async def admin_back(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    user = callback.from_user
    lang = await get_user_language(user.id) or 'ru'
    await callback.message.edit_text(t('welcome', lang), reply_markup=main_keyboard(lang))
    await callback.answer()
