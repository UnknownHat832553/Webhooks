import requests
import schedule
import time
from datetime import datetime, timedelta
import pytz

WEBHOOK_URL = "https://discord.com/api/webhooks/1369696308255789087/kT8rUk5ipDa5QF0ndZAeru0pb2bDysUDkMD-Clzjoj52UL9sqfsh7CmIBq1h4kP_H6FT"
NEWS_API_KEY = "51ff845da43d4f89945619257c764ce4"
NEWS_URL = f"https://newsapi.org/v2/top-headlines?country=th&apiKey={NEWS_API_KEY}"

def news():
    print("รัน news แล้วจ้า!", datetime.now().strftime("%H:%M:%S"))
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

test_time = (datetime.now() + timedelta(minutes=1)).strftime("%H:%M")
print(f"จะเทสต์ส่งข่าวตอน: {test_time}")
schedule.every().day.at(test_time).do(news)

while True:
    schedule.run_pending()
    time.sleep(30)
