import asyncio
asyncio.set_event_loop(asyncio.new_event_loop())

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import os

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

BASE_URL = "https://filestreambot-skvy.onrender.com"

bot = Client(
    "filestreambot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@bot.on_message(filters.command("start"))
async def start(client, message):

    await message.reply_text(
        "🤖 File Stream Bot Ready\n\nSend any file to generate stream link."
    )


@bot.on_message(filters.video | filters.document)
async def get_file(client, message):

    file_id = message.video.file_id if message.video else message.document.file_id

    link = f"{BASE_URL}/watch/{file_id}?user={message.from_user.id}"

    buttons = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "🔓 Watch 2 Ads To Unlock",
                    url=link
                )
            ]
        ]
    )

    await message.reply_text(
        "📁 File received\n\nWatch 2 ads to unlock link",
        reply_markup=buttons
    )


print("Bot Started")

bot.run()
