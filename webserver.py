from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"status": "bot running"}

@app.get("/watch/{file_id}")
def watch(file_id: str):
    return {
        "stream_file_id": file_id,
        "message": "Streaming system working"
    }
