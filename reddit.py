import requests
import json
import time

REDDIT_URL = "https://www.reddit.com/r/kickopenthedoor/.json"
HEADERS = {"User-Agent": "KickDoorQOL/0.1"}

def get_active_bosses():
    response = requests.get(REDDIT_URL, headers=HEADERS)
    data = response.json();
    timestamp = int(time.time())
    with open(f"reddit_dump_{timestamp}.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

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
                "url": url,
                "created_utc": data["created_utc"],
                "flair": flair,
                "stars": flair.count("★"),
                "health": flair.split("★")[-1],
                "imageUrl": image_url,
            })

    bosses.sort(key=lambda x: x["created_utc"], reverse=True)
    return bosses