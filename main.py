import asyncio
import logging
from aiohttp import web
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties

from config import BOT_TOKEN, HTTP_HOST, HTTP_PORT
from database import init_db
from handlers import start_router, admin_router
from http_server import make_http_app

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


async def main():
    await init_db()

    bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()

    dp.include_router(start_router)
    dp.include_router(admin_router)

    http_app = make_http_app(bot)
    runner = web.AppRunner(http_app)
    await runner.setup()
    site = web.TCPSite(runner, HTTP_HOST, HTTP_PORT)
    await site.start()
    log.info('Customer bot HTTP server listening on %s:%s', HTTP_HOST, HTTP_PORT)

    await bot.delete_webhook(drop_pending_updates=True)
    try:
        await dp.start_polling(bot)
    finally:
        await runner.cleanup()


if __name__ == '__main__':
    asyncio.run(main())
