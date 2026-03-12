import asyncio
asyncio.set_event_loop(asyncio.new_event_loop())

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import os

API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")

BOT_USERNAME = "filesstreams_bot"   # अपना bot username डालें
BASE_URL = "https://filestreambot-skvy.onrender.com"

bot = Client(
    "filestreambot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# file receive
@bot.on_message(filters.video | filters.document)
async def get_file(client, message):

    if message.video:
        file_id = message.video.file_id
    else:
        file_id = message.document.file_id

    unlock_url = f"{BASE_URL}/unlock/{file_id}"

    keyboard = InlineKeyboardMarkup(
        [[InlineKeyboardButton("🔓 Watch 2 Ads To Unlock", url=unlock_url)]]
    )

    await message.reply_text(
        "⚠️ Watch 2 ads to unlock video link",
        reply_markup=keyboard
    )

# start command (ads देखने के बाद)
@bot.on_message(filters.command("start"))
async def start(client, message):

    data = message.text.split(" ")

    if len(data) > 1:

        file_id = data[1]

        link = f"{BASE_URL}/watch/{file_id}"

        await message.reply_text(
            f"🎬 Stream Link\n{link}"
        )

    else:
        await message.reply_text(
            "Send me a video or file to generate stream link."
        )

bot.run()
