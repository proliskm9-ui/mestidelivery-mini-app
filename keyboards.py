from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from texts import t, CUSTOM_EMOJI
from config import WEBAPP_URL, MINIAPP_URL, SUPPORT_URL


def _btn(text: str, emoji_key: str, **kwargs) -> InlineKeyboardButton:
    return InlineKeyboardButton(
        text=text,
        icon_custom_emoji_id=str(CUSTOM_EMOJI[emoji_key]),
        **kwargs,
    )


def language_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            _btn('Русский', 'flag_ru', callback_data='lang_ru'),
            _btn('English', 'flag_en', callback_data='lang_en'),
        ],
        [_btn('ქართული', 'flag_ka', callback_data='lang_ka')],
    ])


def main_keyboard(lang: str = 'ru') -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(
            text=t('open', lang),
            icon_custom_emoji_id=str(CUSTOM_EMOJI['order']),
            web_app=WebAppInfo(url=MINIAPP_URL),
        )],
        [
            _btn(t('change_lang', lang), 'lang', callback_data='change_lang'),
            _btn(t('support', lang), 'support', url=SUPPORT_URL),
        ],
        [_btn(t('web', lang), 'web', url=WEBAPP_URL)],
    ])


def admin_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='📊 Статистика', callback_data='admin_stats')],
        [InlineKeyboardButton(text='📨 Рассылка', callback_data='admin_broadcast')],
        [InlineKeyboardButton(text='◀️ В меню бота', callback_data='admin_back')],
    ])


def broadcast_audience_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            _btn('Русский', 'flag_ru', callback_data='broadcast_aud_ru'),
            _btn('English', 'flag_en', callback_data='broadcast_aud_en'),
        ],
        [_btn('ქართული', 'flag_ka', callback_data='broadcast_aud_ka')],
        [InlineKeyboardButton(text='🌍 Все пользователи', callback_data='broadcast_aud_all')],
        [InlineKeyboardButton(text='◀️ Назад', callback_data='admin_menu')],
    ])


def broadcast_confirm_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text='✅ Отправить', callback_data='broadcast_confirm'),
            InlineKeyboardButton(text='❌ Отмена', callback_data='broadcast_cancel'),
        ],
        [InlineKeyboardButton(text='◀️ Назад', callback_data='admin_menu')],
    ])
