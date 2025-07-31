import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from youtube.audio_downloader import download_audio

# Put a video id for testing purposes :)
video_url = "https://www.youtube.com/watch?v=6BfEEwrHJH4"
video_id = "6BfEEwrHJH4"

if __name__ == "__main__":
    path = download_audio(video_url, video_id)
    print(f"✅ Downloaded audio to: {path}")
