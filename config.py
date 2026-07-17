import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN', '')
WEBAPP_URL = os.getenv('WEBAPP_URL', 'https://mestidelivery.web.app/')
MINIAPP_URL = os.getenv('MINIAPP_URL', '') or WEBAPP_URL
SUPPORT_URL = os.getenv('SUPPORT_URL', 'https://t.me/MestigoSupport_Bot')
ADMIN_IDS = [int(x) for x in os.getenv('ADMIN_IDS', '').split(',') if x.strip().isdigit()]
DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite+aiosqlite:///bot.db')
BOT_SECURITY_TOKEN = os.getenv('BOT_SECURITY_TOKEN', os.getenv('CLIENT_BOT_SECURITY_TOKEN', ''))
HTTP_HOST = os.getenv('HTTP_HOST', '0.0.0.0')
HTTP_PORT = int(os.getenv('HTTP_PORT', '50062'))
