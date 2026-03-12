echo "Starting Telegram Bot..."
python bot.py &

echo "Starting Web Server..."
uvicorn webserver:app --host 0.0.0.0 --port 10000
