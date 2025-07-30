# test_watch.py

import json
from youtube.watcher import fetch_new_videos_from_channels

def load_channels():
    with open("data/channels.json", "r") as f:
        return json.load(f)

if __name__ == "__main__":
    channels = load_channels()
    new_videos = fetch_new_videos_from_channels(channels)

    if new_videos:
        print("🆕 New videos found:")
        for video in new_videos:
            print(f"  • {video['channel']} - {video['title']} ({video['url']})")
    else:
        print("✅ No new videos.")
