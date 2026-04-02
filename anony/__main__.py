import asyncio
import importlib
import os
from threading import Thread
from flask import Flask

from pyrogram import idle
from anony import app, db, logger
from anony.modules import all_modules


# Flask app
web_app = Flask('')

@web_app.route('/')
def home():
    return "Bot is running!"

def run_web():
    PORT = int(os.environ.get("PORT", 5000))
    web_app.run(host='0.0.0.0', port=PORT)


async def anony_boot():
    try:
        await app._start()
        print("Bot Started ✅")
    except Exception as ex:
        print("Bot Error ❌:", ex)
        return

    await db.connect()

    for module in all_modules:
        importlib.import_module(f"anony.modules.{module}")
    logger.info(f"Loaded {len(all_modules)} modules.")

    await idle()
    await app._stop()
    await db.close()


if __name__ == "__main__":
    # 🔥 Flask ko yaha start karo
    Thread(target=run_web).start()

    asyncio.get_event_loop().run_until_complete(anony_boot())
    logger.info("Stopping String Gen Bot...")
