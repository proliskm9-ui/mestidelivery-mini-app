from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart

from database import get_or_create_user, set_user_language, get_user_language
from keyboards import language_keyboard, main_keyboard
from texts import t

router = Router()


async def send_choose(message: Message, first_name: str) -> None:
    await message.answer(
        t('choose', 'en', first_name),
        parse_mode='HTML',
        reply_markup=language_keyboard(),
    )


async def send_welcome(message: Message, lang: str) -> None:
    await message.answer(
        t('welcome', lang),
        parse_mode='HTML',
        reply_markup=main_keyboard(lang),
    )


@router.message(CommandStart())
async def cmd_start(message: Message):
    user = message.from_user
    await get_or_create_user(user.id, user.username, user.first_name, user.last_name)
    lang = await get_user_language(user.id)

    if lang:
        await send_welcome(message, lang)
    else:
        await send_choose(message, user.first_name)


@router.callback_query(F.data.startswith('lang_'))
async def set_language(callback: CallbackQuery):
    lang = callback.data.split('_')[1]
    await set_user_language(callback.from_user.id, lang)

    try:
        await callback.message.delete()
    except Exception:
        pass

    await send_welcome(callback.message, lang)
    await callback.answer('✅')


@router.callback_query(F.data == 'change_lang')
async def change_language(callback: CallbackQuery):
    lang = await get_user_language(callback.from_user.id) or 'en'

    try:
        await callback.message.delete()
    except Exception:
        pass

    await callback.message.answer(
        t('choose', lang, callback.from_user.first_name),
        parse_mode='HTML',
        reply_markup=language_keyboard(),
    )
    await callback.answer()
