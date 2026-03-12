import asyncio
import os

# Fix for Pyrogram event loop error
asyncio.set_event_loop(asyncio.new_event_loop())

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import uvicorn

API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")

BASE_URL = "https://filestreambot-skvy.onrender.com"

PORT = int(os.environ.get("PORT", 10000))

app = FastAPI()

bot = Client(
    "filestreambot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@bot.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text(
        "🚀 File Stream Bot Working\n\nSend a file to generate stream link."
    )

@bot.on_message(filters.video | filters.document)
async def get_file(client, message):

    if message.video:
        file_id = message.video.file_id
    else:
        file_id = message.document.file_id

    link = f"{BASE_URL}/ads/{file_id}?user={message.from_user.id}"

    button = InlineKeyboardMarkup(
        [[InlineKeyboardButton("🎬 Watch 2 Ads to Unlock", url=link)]]
    )

    await message.reply_text(
        "🔒 Watch 2 ads to unlock your streaming link",
        reply_markup=button
    )

@app.get("/")
async def home():
    return {"status": "Bot running"}

@app.get("/ads/{file_id}")
async def ads_page(file_id: str, user: int):

    html = f"""
    <html>
    <body style="text-align:center">

    <h2>Watch Ads to Unlock</h2>

    <script src='//libtl.com/sdk.js'
    data-zone='10555415'
    data-sdk='show_10555415'></script>

    <button onclick="show_10555415()">Watch Ad</button>

    <br><br>

    <a href="/watch/{file_id}?user={user}">Continue</a>

    </body>
    </html>
    """

    return HTMLResponse(html)

@app.get("/watch/{file_id}")
async def watch(file_id: str):

    html = """
    <html>
    <body style="text-align:center">
    <h2>Stream Ready</h2>
    </body>
    </html>
    """

    return HTMLResponse(html)

async def main():

    await bot.start()
    print("BOT STARTED")

    config = uvicorn.Config(app, host="0.0.0.0", port=PORT)
    server = uvicorn.Server(config)

    asyncio.create_task(server.serve())

    await bot.idle()

if __name__ == "__main__":
    asyncio.run(main())
