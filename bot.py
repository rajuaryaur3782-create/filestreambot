import asyncio
asyncio.set_event_loop(asyncio.new_event_loop())

from pyrogram import Client, filters
import os

API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")

bot = Client(
    "filestreambot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@bot.on_message(filters.video | filters.document)
async def get_file(client, message):

    if message.video:
        file_id = message.video.file_id
    else:
        file_id = message.document.file_id

    link = f"https://filestreambot-skvy.onrender.com/watch/{file_id}"

    await message.reply_text(
        f"🎬 Stream Link\n{link}"
    )

print("Bot Started Successfully")

bot.run()
