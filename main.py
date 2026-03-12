import asyncio
import os

asyncio.set_event_loop(asyncio.new_event_loop())

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import uvicorn

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

BASE_URL = "https://filestreambot-skvy.onrender.com"

app = FastAPI()

bot = Client(
    "filestreambot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

ad_counter = {}


@bot.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text(
        "🤖 File Stream Bot Working\n\nSend a file to generate stream link."
    )


@bot.on_message(filters.video | filters.document)
async def get_file(client, message):

    file_id = message.video.file_id if message.video else message.document.file_id

    link = f"{BASE_URL}/watch/{file_id}?user={message.from_user.id}"

    buttons = InlineKeyboardMarkup(
        [[InlineKeyboardButton("🔓 Watch 2 Ads To Unlock", url=link)]]
    )

    await message.reply_text(
        "📁 File received\nWatch 2 ads to unlock link",
        reply_markup=buttons
    )


@app.get("/")
async def home():
    return {"status": "bot running"}


@app.get("/watch/{file_id}", response_class=HTMLResponse)
async def watch(file_id: str, user: int):

    if user not in ad_counter:
        ad_counter[user] = 0

    if ad_counter[user] < 2:
        ad_counter[user] += 1
        remaining = 2 - ad_counter[user]

        return f"""
        <html>
        <body style="text-align:center">
        <h2>Watch Ad</h2>

        <script src='//libtl.com/sdk.js'
        data-zone='10555415'
        data-sdk='show_10555415'></script>

        <button onclick="show_10555415()">Watch Ad</button>

        <h3>{remaining} more ad required</h3>

        <a href="/watch/{file_id}?user={user}">Continue</a>
        </body>
        </html>
        """

    else:
        return """
        <html>
        <body style="text-align:center">
        <h2>Ads Completed</h2>
        </body>
        </html>
        """


async def main():
    await bot.start()

    config = uvicorn.Config(app, host="0.0.0.0", port=10000)
    server = uvicorn.Server(config)

    await server.serve()


if __name__ == "__main__":
    asyncio.run(main())
