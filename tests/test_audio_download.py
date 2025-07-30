import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from youtube.audio_downloader import download_audio

# Never Gonna Give You Up by Rick Astley for testing purposes :)
video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
video_id = "dQw4w9WgXcQ"

if __name__ == "__main__":
    path = download_audio(video_url, video_id)
    print(f"✅ Downloaded audio to: {path}")
