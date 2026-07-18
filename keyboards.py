from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from texts import t, CUSTOM_EMOJI
from admin_texts import ADMIN_EMOJI
from config import WEBAPP_URL, MINIAPP_URL, SUPPORT_URL


def _btn(text: str, emoji_key: str, **kwargs) -> InlineKeyboardButton:
    return InlineKeyboardButton(
        text=text,
        icon_custom_emoji_id=str(CUSTOM_EMOJI[emoji_key]),
        **kwargs,
    )


def _admin_btn(text: str, emoji_key: str, **kwargs) -> InlineKeyboardButton:
    return InlineKeyboardButton(
        text=text,
        icon_custom_emoji_id=str(ADMIN_EMOJI[emoji_key]),
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
        [_admin_btn('Статистика', 'stats', callback_data='admin_stats')],
        [_admin_btn('Рассылка', 'broadcast', callback_data='admin_broadcast')],
        [_admin_btn('В меню бота', 'phone', callback_data='admin_back')],
    ])


def broadcast_audience_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            _btn('Русский', 'flag_ru', callback_data='broadcast_aud_ru'),
            _btn('English', 'flag_en', callback_data='broadcast_aud_en'),
        ],
        [_btn('ქართული', 'flag_ka', callback_data='broadcast_aud_ka')],
        [_admin_btn('Все пользователи', 'all', callback_data='broadcast_aud_all')],
        [_admin_btn('Назад', 'point', callback_data='admin_menu')],
    ])


def broadcast_confirm_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            _admin_btn('Отправить', 'done', callback_data='broadcast_confirm'),
            InlineKeyboardButton(text='❌ Отмена', callback_data='broadcast_cancel'),
        ],
        [_admin_btn('Назад', 'point', callback_data='admin_menu')],
    ])
