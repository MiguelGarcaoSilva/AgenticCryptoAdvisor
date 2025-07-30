# youtube/watcher.py

import requests
import xml.etree.ElementTree as ET
import json
import os

SEEN_FILE = "data/seen_videos.json"

def fetch_new_videos_from_channels(channels, max_results=5):
    all_new_videos = []

    for channel in channels:
        channel_id = channel["channel_id"]
        channel_name = channel["name"]
        rss_url = f"https://www.youtube.com/feeds/videos.xml?channel_id={channel_id}"

        try:
            response = requests.get(rss_url)
            response.raise_for_status()
        except Exception as e:
            print(f"❌ Failed to fetch RSS for {channel_name}: {e}")
            continue

        root = ET.fromstring(response.content)
        entries = root.findall("{http://www.w3.org/2005/Atom}entry")

        for entry in entries[:max_results]:
            video_id = entry.find("{http://www.youtube.com/xml/schemas/2015}videoId").text

            if video_id in load_seen_ids():
                continue

            title = entry.find("{http://www.w3.org/2005/Atom}title").text
            link = entry.find("{http://www.w3.org/2005/Atom}link").attrib["href"]
            published = entry.find("{http://www.w3.org/2005/Atom}published").text

            all_new_videos.append({
                "id": video_id,
                "channel": channel_name,
                "title": title,
                "url": link,
                "published": published
            })

    # Save the new video IDs so we don't fetch them again
    update_seen_ids([v["id"] for v in all_new_videos])
    return all_new_videos


def load_seen_ids():
    if not os.path.exists(SEEN_FILE):
        return set()
    with open(SEEN_FILE, "r") as f:
        return set(json.load(f))


def update_seen_ids(new_ids):
    seen = load_seen_ids()
    seen.update(new_ids)
    with open(SEEN_FILE, "w") as f:
        json.dump(list(seen), f)
