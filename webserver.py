from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse

app = FastAPI()

ad_counter = {}

@app.get("/")
async def home():
    return {"status": "bot running"}

# ADD THIS (uptimerobot fix)
@app.head("/")
async def head():
    return JSONResponse(content={"status": "ok"})


@app.get("/watch/{file_id}", response_class=HTMLResponse)
async def watch(file_id: str, user: int):

    if user not in ad_counter:
        ad_counter[user] = 0

    ads_seen = ad_counter[user]

    if ads_seen < 2:
        ad_counter[user] += 1
        remaining = 2 - ad_counter[user]

        return f"""
        <html>
        <body style="text-align:center">
        <h2>Watch Ad {ads_seen+1}</h2>

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
        return f"""
        <html>
        <body style="text-align:center">
        <h2>Ads Completed</h2>
        <p>Stream Unlocked</p>
        </body>
        </html>
        """
