import json
import time
from urllib.parse import quote, unquote

import requests

REDDIT_URL = "https://www.reddit.com/r/kickopenthedoor/.json"
HEADERS = {"User-Agent": "KickDoorQOL/0.1"}

RANGE = "\ud83c\udff9"
MELEE = "\u2694\ufe0f"
MAGIC = "\ud83d\udd2e"
STAR = "\u2605"
HEART = "\u2764\ufe0f"

def get_active_bosses():
    response = requests.get(REDDIT_URL, headers=HEADERS)
    data = response.json()
    # timestamp = int(time.time())
    # with open(f"reddit_dump_{timestamp}.json", "w", encoding="utf-8") as f:
    #     json.dump(data, f, indent=2)

    posts = data["data"]["children"]
    bosses = []

    for post in posts:
        data = post["data"]
        title = data.get("title", "").lower()
        flair = data.get("link_flair_text", "")
        url = f"https://reddit.com{data.get('permalink')}"

        # Try preview image first
        if "preview" in data and "images" in data["preview"]:
            image_url = data["preview"]["images"][0]["source"]["url"].replace("&amp;", "&")

        # Fallback to thumbnail
        elif data.get("thumbnail") and data["thumbnail"].startswith("http"):
            image_url = data["thumbnail"]


        if "boss" in title or (flair and "❤️" in flair.lower()):
            bosses.append({
                "title": data["title"],
                "url": quote(url, safe=''),
                "created_utc": data["created_utc"],
                "flair": flair,
                "stars": flair.count(STAR),
                "health": flair.split(STAR)[-1],
                "imageUrl": image_url,
                "attackType": flair.split(" ")[0]
            })

    bosses.sort(key=lambda x: x["created_utc"], reverse=True)
    return bosses


def get_boss_stats(url):
    json_url = unquote(url) + ".json"
    response = requests.get(json_url, headers=HEADERS)
    data = response.json()
    timestamp = int(time.time())
    with open(f"reddit_post_dump_{timestamp}.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    return len(data)
