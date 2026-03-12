import asyncio
asyncio.set_event_loop(asyncio.new_event_loop())

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import os

API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")

BASE_URL = "https://filestreambot-skvy.onrender.com"
BOT_USERNAME = "filesstreams_bot"

bot = Client(
    "filestreambot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@bot.on_message(filters.video | filters.document)
async def file_handler(client, message):

    if message.video:
        file_id = message.video.file_id
    else:
        file_id = message.document.file_id

    unlock = f"{BASE_URL}/unlock/{file_id}"

    buttons = InlineKeyboardMarkup(
        [[InlineKeyboardButton("🔓 Watch 2 Ads To Unlock", url=unlock)]]
    )

    await message.reply_text(
        "⚠️ Watch 2 ads to unlock your video link",
        reply_markup=buttons
    )


@bot.on_message(filters.command("start"))
async def start(client, message):

    data = message.text.split(" ")

    if len(data) > 1:

        file_id = data[1]

        link = f"{BASE_URL}/watch/{file_id}"

        buttons = InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("🎬 Watch Video", url=link)],
                [InlineKeyboardButton("⬇ Download", url=link)],
                [InlineKeyboardButton("📱 Open In MX Player", url=link)]
            ]
        )

        await message.reply_text(
            "🎉 Video Unlocked!",
            reply_markup=buttons
        )

    else:
        await message.reply_text(
            "Send me a video or file to generate stream link."
        )

bot.run()
