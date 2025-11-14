import time
import requests

URL = "https://telegram-bot-1dl7.onrender.com"  # твой Render URL

while True:
    try:
        requests.get(URL)
        print("KeepAlive: ping OK")
    except Exception as e:
        print("KeepAlive error:", e)
    time.sleep(300)  # 5 минут
