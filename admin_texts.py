from texts import e, CUSTOM_EMOJI

# Пак кастомных эмодзи (нумерация ID с конца пака):
# bag, trophy, phone, hearts, hand, app, speech, laptop, banknotes, exchange, coin
ADMIN_EMOJI = {
    'panel': '5384244502040975393',       # app icon → 🔐
    'point': '5382351125838077755',       # coin → 👇
    'stats': '5382248944271140910',       # trophy → 📊
    'users': '5384222159621102491',       # hearts → 👥
    'new': '5384312315279612142',         # shopping bag → 🆕
    'broadcast': '5382097310450753507',   # speech bubble → 📨
    'sent': '5381848533060067195',        # laptop → 📤
    'done': '5384489194917765397',        # hand → ✅
    'all': '5384518714227990146',         # exchange → 🌍
    'money': '5384520939021048827',       # banknotes
    'phone': '5384138412053796842',       # smartphone
    'flag_ru': CUSTOM_EMOJI['flag_ru'],
    'flag_en': CUSTOM_EMOJI['flag_en'],
    'flag_ka': CUSTOM_EMOJI['flag_ka'],
}


def _ae(key: str, alt: str) -> str:
    return e(ADMIN_EMOJI[key], alt)


AUDIENCE_LABELS = {
    'ru': f'{_ae("flag_ru", "🇷🇺")} Русский',
    'en': f'{_ae("flag_en", "🇬🇧")} English',
    'ka': f'{_ae("flag_ka", "🇬🇪")} ქართული',
    'all': f'{_ae("all", "🌍")} Все пользователи',
}


def admin_panel_text() -> str:
    return (
        f'{_ae("panel", "🔐")} <b>Админ-панель</b>\n'
        '<i>MestiDelivery Bot</i>\n\n'
        f'Выберите действие {_ae("point", "👇")}'
    )


def admin_stats_text(stats: dict, lang_stats: dict) -> str:
    return (
        f'{_ae("stats", "📊")} <b>Статистика</b>\n\n'
        f'{_ae("users", "👥")} Всего пользователей: <b>{stats["total"]}</b>\n'
        f'{_ae("new", "🆕")} Новых сегодня: <b>{stats["today"]}</b>\n\n'
        '<b>По языкам:</b>\n'
        f'{_ae("flag_ru", "🇷🇺")} Русский — <b>{lang_stats["ru"]}</b>\n'
        f'{_ae("flag_en", "🇬🇧")} English — <b>{lang_stats["en"]}</b>\n'
        f'{_ae("flag_ka", "🇬🇪")} ქართული — <b>{lang_stats["ka"]}</b>\n'
        f'❓ Без языка — <b>{lang_stats["none"]}</b>'
    )


def broadcast_choose_audience_text() -> str:
    return (
        f'{_ae("broadcast", "📨")} <b>Рассылка</b>\n\n'
        'Выберите <b>аудиторию</b> — сообщение получат только пользователи с выбранным языком.\n\n'
        f'<i>Например, акции для грузин — только {_ae("flag_ka", "🇬🇪")} ქართული</i>'
    )


def broadcast_waiting_text(audience: str, recipients: int) -> str:
    label = AUDIENCE_LABELS.get(audience, audience)
    return (
        f'{_ae("broadcast", "📨")} <b>Рассылка</b>\n\n'
        f'Аудитория: <b>{label}</b>\n'
        f'Получателей: <b>{recipients}</b>\n\n'
        'Отправьте сообщение для рассылки\n'
        '<i>(текст, фото или видео)</i>'
    )


def broadcast_confirm_text(audience: str, recipients: int) -> str:
    label = AUDIENCE_LABELS.get(audience, audience)
    return (
        f'{_ae("broadcast", "📨")} <b>Подтвердите рассылку</b>\n\n'
        f'Аудитория: <b>{label}</b>\n'
        f'Получателей: <b>{recipients}</b>\n\n'
        'Отправить?'
    )


def broadcast_done_text(audience: str, success: int, failed: int) -> str:
    label = AUDIENCE_LABELS.get(audience, audience)
    return (
        f'{_ae("done", "✅")} <b>Рассылка завершена</b>\n\n'
        f'Аудитория: <b>{label}</b>\n'
        f'{_ae("sent", "📤")} Отправлено: <b>{success}</b>\n'
        f'❌ Ошибок: <b>{failed}</b>'
    )


def broadcast_started_text() -> str:
    return f'{_ae("sent", "⏳")} Рассылка началась...'


def broadcast_cancelled_text() -> str:
    return '❌ Рассылка отменена'
