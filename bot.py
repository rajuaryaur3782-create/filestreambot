from pyrogram import Client, filters
import os

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Client(
    "filestreambot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@bot.on_message(filters.video | filters.document)
async def get_file(client, message):

    file_id = message.video.file_id if message.video else message.document.file_id

    link = f"https://yourapp.onrender.com/watch/{file_id}"

    await message.reply_text(
        f"🎬 Stream Link\n{link}"
    )

bot.run()