CUSTOM_EMOJI = {
    'welcome': '5384489194917765397',
    'first': '5384312315279612142',
    'mestia': '5384222159621102491',
    'order': '5384138412053796842',
    'lang': '5382351125838077755',
    'point_down': '5382351125838077755',
    'support': '5382097310450753507',
    'web': '5381848533060067195',
    'flag_ru': '5449408995691341691',
    'flag_en': '5202196682497859879',
    'flag_ka': '5440371950708864925',
}


def e(emoji_id: str, alt: str) -> str:
    return f'<tg-emoji emoji-id="{emoji_id}">{alt}</tg-emoji>'


TEXTS = {
    'ru': {
        'choose': lambda first_name: f'''{e(CUSTOM_EMOJI['welcome'], '👋')} Добро пожаловать, <b>{first_name}</b>!

{e(CUSTOM_EMOJI['first'], '💚')} Это <b>первый в Сванетии сервис доставки еды</b>. Лучшие рестораны и магазины Местии — <b>в одном месте</b>.

Чтобы продолжить, выберите язык {e(CUSTOM_EMOJI['point_down'], '👇')}''',
        'welcome': f'''{e(CUSTOM_EMOJI['mestia'], '⛰')} Местия умеет удивлять не только видами, <b>но и вкусами</b>.

Наслаждайтесь отдыхом в Местии — <b>о вкусной еде мы позаботимся</b>. Доставим любимые блюда быстро и с заботой о качестве.''',
        'open': 'СДЕЛАТЬ ЗАКАЗ',
        'change_lang': 'Сменить язык',
        'support': 'Поддержка',
        'web': 'MestiDelivery Web',
    },
    'en': {
        'choose': lambda first_name: f'''{e(CUSTOM_EMOJI['welcome'], '👋')} Welcome, <b>{first_name}</b>!

{e(CUSTOM_EMOJI['first'], '💚')} This is <b>the first food delivery service in Svaneti</b>. The best restaurants and shops in Mestia are gathered <b>in one place</b>.

Please choose a language to continue {e(CUSTOM_EMOJI['point_down'], '👇')}''',
        'welcome': f'''{e(CUSTOM_EMOJI['mestia'], '⛰')} Mestia can surprise not only with views, <b>but also with flavors</b>.

Enjoy your time — <b>we'll take care of the food</b>. Fast delivery with attention to quality.''',
        'open': 'PLACE AN ORDER',
        'change_lang': 'Change language',
        'support': 'Support',
        'web': 'MestiDelivery Web',
    },
    'ka': {
        'choose': lambda first_name: f'''{e(CUSTOM_EMOJI['welcome'], '👋')} გამარჯობა, <b>{first_name}</b>!

{e(CUSTOM_EMOJI['first'], '💚')} ეს არის <b>სვანეთში პირველი საკვების მიტანის სერვისი</b>. მესტიის საუკეთესო რესტორნები და მაღაზიები — <b>ყველაფერი ერთ სივრცეში</b>.

გაგრძელებისთვის აირჩიეთ თქვენი ენა {e(CUSTOM_EMOJI['point_down'], '👇')}''',
        'welcome': f'''{e(CUSTOM_EMOJI['mestia'], '⛰')} მესტიამ შეიძლება გაგაოცოთ არა მხოლოდ თავისი ხედებით,
<b>არამედ თავისი გემოებითაც</b>.

ისიამოვნეთ შვებულებით მესტიაში — <b>ჩვენ კი უგემრიელესი საკვებით ვიზრუნებთ</b>. ჩვენ მოგაწვდით თქვენს საყვარელ კერძებს სწრაფად და ხარისხზე ზრუნვით.''',
        'open': 'შეკვეთა',
        'change_lang': 'ენის შეცვლა',
        'support': 'მხარდაჭერა',
        'web': 'MestiDelivery Web',
    },
}


def t(key: str, lang: str = 'ru', first_name: str = None):
    texts = TEXTS.get(lang, TEXTS['ru'])
    value = texts.get(key, TEXTS['ru'].get(key, key))
    if callable(value) and first_name:
        return value(first_name)
    return value
