from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

BOT_USERNAME = "filesstreams_bot"

@app.get("/")
def home():
    return {"status": "bot running"}

# ads unlock page
@app.get("/unlock/{file_id}", response_class=HTMLResponse)
def unlock(file_id: str):

    html = f"""
    <html>
    <head>

    <title>Unlock Link</title>

    <script src='//libtl.com/sdk.js'
    data-zone='10555415'
    data-sdk='show_10555415'></script>

    <script>

    var ads = 0;

    function watchAd() {{

        show_10555415().then(() => {{

            ads++;

            if(ads >= 2){{
                window.location.href="https://t.me/{BOT_USERNAME}?start={file_id}"
            }}

        }});
    }}

    </script>

    </head>

    <body style="text-align:center;font-family:sans-serif">

    <h2>Watch 2 Ads To Unlock Link</h2>

    <button onclick="watchAd()" style="padding:15px;font-size:18px">
    Watch Ad
    </button>

    </body>
    </html>
    """

    return html


# video page
@app.get("/watch/{file_id}", response_class=HTMLResponse)
def watch(file_id: str):

    html = f"""
    <html>

    <body style="text-align:center">

    <h2>Video Player</h2>

    <p>Your file id:</p>

    <p>{file_id}</p>

    </body>

    </html>
    """

    return html
