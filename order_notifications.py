ORDER_STATUS_TEXTS = {
    'accepted': {
        'ru': '✅ <b>Заказ #{order_id} принят</b>\n\nРесторан <b>{restaurant_name}</b> принял ваш заказ. Скоро начнётся приготовление.',
        'en': '✅ <b>Order #{order_id} accepted</b>\n\n<b>{restaurant_name}</b> has accepted your order. Preparation will start soon.',
        'ka': '✅ <b>შეკვეთა #{order_id} მიღებულია</b>\n\n<b>{restaurant_name}</b> მიიღო თქვენი შეკვეთა. მალე დაიწყება მომზადება.',
    },
    'preparing': {
        'ru': '👨‍🍳 <b>Заказ #{order_id} готовится</b>\n\nВаш заказ уже готовят в <b>{restaurant_name}</b>.',
        'en': '👨‍🍳 <b>Order #{order_id} is being prepared</b>\n\nYour order is now being prepared at <b>{restaurant_name}</b>.',
        'ka': '👨‍🍳 <b>შეკვეთა #{order_id} მზადდება</b>\n\nთქვენი შეკვეთა უკვე მზადდება <b>{restaurant_name}</b>-ში.',
    },
    'prep_delayed': {
        'ru': (
            '⏱ <b>Заказ #{order_id}: ресторан просит чуть больше времени</b>\n\n'
            '<b>{restaurant_name}</b> загружен. Ожидаемое время обработки: '
            '<b>+{delay_minutes} мин</b> (до {until_time}).'
        ),
        'en': (
            '⏱ <b>Order #{order_id}: restaurant needs a bit more time</b>\n\n'
            '<b>{restaurant_name}</b> is busy. Expected processing time: '
            '<b>+{delay_minutes} min</b> (until {until_time}).'
        ),
        'ka': (
            '⏱ <b>შეკვეთა #{order_id}: რესტორანს მეტი დრო სჭირდება</b>\n\n'
            '<b>{restaurant_name}</b> დატვირთულია. მოსალოდნელი დრო: '
            '<b>+{delay_minutes} წთ</b> ({until_time}-მდე).'
        ),
    },
    'delivering': {
        'ru': '🚗 <b>Заказ #{order_id} в пути</b>\n\nКурьер уже везёт ваш заказ. Следите за статусом в приложении.',
        'en': '🚗 <b>Order #{order_id} is on the way</b>\n\nYour courier is already heading to you. Track the status in the app.',
        'ka': '🚗 <b>შეკვეთა #{order_id} გზაშია</b>\n\nკურიერი უკვე მოგაქვთ შეკვეთას. სტატუსს აკონტროლეთ აპში.',
    },
    'delivered': {
        'ru': '🎉 <b>Заказ #{order_id} доставлен</b>\n\nПриятного аппетита! Спасибо, что выбрали MestiDelivery.',
        'en': '🎉 <b>Order #{order_id} delivered</b>\n\nEnjoy your meal! Thank you for choosing MestiDelivery.',
        'ka': '🎉 <b>შეკვეთა #{order_id} მიტანილია</b>\n\nსასიამოვნო მიღება! გმადლობთ, რომ აირჩიეთ MestiDelivery.',
    },
}


def normalize_language(lang: str) -> str:
    lang = (lang or 'en').lower().strip()
    if lang.startswith('ru'):
        return 'ru'
    if lang.startswith('ka'):
        return 'ka'
    if lang.startswith('en'):
        return 'en'
    if lang in ORDER_STATUS_TEXTS['accepted']:
        return lang
    return 'en'


def format_order_status_message(status: str, language: str, **kwargs) -> str:
    lang = normalize_language(language)
    template = ORDER_STATUS_TEXTS.get(status, {}).get(lang)
    if not template:
        template = ORDER_STATUS_TEXTS.get(status, {}).get('en', 'Order #{order_id} status: {status}')
    kwargs.setdefault('restaurant_name', 'MestiDelivery')
    kwargs.setdefault('order_id', '?')
    kwargs.setdefault('delay_minutes', '?')
    kwargs.setdefault('until_time', '—')
    return template.format(status=status, **kwargs)
