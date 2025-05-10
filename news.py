import requests
import schedule
import time
from datetime import datetime
import pytz
from main import WEBHOOK_URL

NEWS_API_KEY = "51ff845da43d4f89945619257c764ce4"
NEWS_URL = f"https://newsapi.org/v2/top-headlines?country=th&apiKey={NEWS_API_KEY}"

def news():
    response = requests.get(NEWS_URL)
    data = response.json()

    if data["status"] != "ok":
        requests.post(WEBHOOK_URL, json={"content": "ขออภัย:1356827591977472145: ดึงข่าวไม่ได้!"})
        return

    articles = data["articles"][:3]
    tz = pytz.timezone("Asia/Bangkok")
    current_time = datetime.now(tz).strftime("%d-%m-%Y | %H:%M:%S")
    for article in articles:
        embed = {
            "title": article["title"],
            "description": article["description"] or "ไม่มีรายละเอียดจ้า",
            "url": article["url"],
            "color": 15844367,
            "footer": {"text": f"เวลา: {current_time}"},
        }
        if article["urlToImage"]:
            embed["image"] = {"url": article["urlToImage"]}

        payload = {
            "username": "News",
            "avatar_url": "https://cdn-icons-png.flaticon.com/512/1828/1828884.png",
            "embeds": [embed],
        }
        requests.post(WEBHOOK_URL, json=payload)

schedule.every().day.at("06:00").do(news)

while True:
    schedule.run_pending()
    time.sleep(30)