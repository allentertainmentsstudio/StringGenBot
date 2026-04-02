import asyncio
import importlib
import os
from threading import Thread
from flask import Flask

from pyrogram import idle
from anony import app, db, logger
from anony.modules import all_modules


# 🔥 Flask Web Server (Deploy ke liye)
web_app = Flask('')

@web_app.route('/')
def home():
    return "Bot is running!"

def run_web():
    PORT = int(os.environ.get("PORT", 3000))
    web_app.run(host='0.0.0.0', port=PORT)

Thread(target=run_web).start()


async def anony_boot():
    try:
        await app._start()
    except Exception as ex:
        raise RuntimeError(ex)
    await db.connect()

    for module in all_modules:
        importlib.import_module(f"anony.modules.{module}")
    logger.info(f"Loaded {len(all_modules)} modules.")

    await idle()
    await app._stop()
    await db.close()


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(anony_boot())
    logger.info("Stopping String Gen Bot...")
