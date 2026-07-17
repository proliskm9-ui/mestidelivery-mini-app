AUDIENCE_LABELS = {
    'ru': '🇷🇺 Русский',
    'en': '🇬🇧 English',
    'ka': '🇬🇪 ქართული',
    'all': '🌍 Все пользователи',
}


def admin_panel_text() -> str:
    return (
        '🔐 <b>Админ-панель</b>\n'
        '<i>MestiDelivery Bot</i>\n\n'
        'Выберите действие 👇'
    )


def admin_stats_text(stats: dict, lang_stats: dict) -> str:
    return (
        '📊 <b>Статистика</b>\n\n'
        f'👥 Всего пользователей: <b>{stats["total"]}</b>\n'
        f'🆕 Новых сегодня: <b>{stats["today"]}</b>\n\n'
        '<b>По языкам:</b>\n'
        f'🇷🇺 Русский — <b>{lang_stats["ru"]}</b>\n'
        f'🇬🇧 English — <b>{lang_stats["en"]}</b>\n'
        f'🇬🇪 ქართული — <b>{lang_stats["ka"]}</b>\n'
        f'❓ Без языка — <b>{lang_stats["none"]}</b>'
    )


def broadcast_choose_audience_text() -> str:
    return (
        '📨 <b>Рассылка</b>\n\n'
        'Выберите <b>аудиторию</b> — сообщение получат только пользователи с выбранным языком.\n\n'
        '<i>Например, акции для грузин — только 🇬🇪 ქართული</i>'
    )


def broadcast_waiting_text(audience: str, recipients: int) -> str:
    label = AUDIENCE_LABELS.get(audience, audience)
    return (
        f'📨 <b>Рассылка</b>\n\n'
        f'Аудитория: <b>{label}</b>\n'
        f'Получателей: <b>{recipients}</b>\n\n'
        'Отправьте сообщение для рассылки\n'
        '<i>(текст, фото или видео)</i>'
    )


def broadcast_confirm_text(audience: str, recipients: int) -> str:
    label = AUDIENCE_LABELS.get(audience, audience)
    return (
        '📨 <b>Подтвердите рассылку</b>\n\n'
        f'Аудитория: <b>{label}</b>\n'
        f'Получателей: <b>{recipients}</b>\n\n'
        'Отправить?'
    )


def broadcast_done_text(audience: str, success: int, failed: int) -> str:
    label = AUDIENCE_LABELS.get(audience, audience)
    return (
        '✅ <b>Рассылка завершена</b>\n\n'
        f'Аудитория: <b>{label}</b>\n'
        f'📤 Отправлено: <b>{success}</b>\n'
        f'❌ Ошибок: <b>{failed}</b>'
    )
