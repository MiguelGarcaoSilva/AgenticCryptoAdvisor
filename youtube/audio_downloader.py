# youtube/downloader.py

import os
import subprocess
from config import AUDIO_DIR

def download_audio(video_url: str, video_id: str) -> str:
    os.makedirs(AUDIO_DIR, exist_ok=True)
    output_path = os.path.join(AUDIO_DIR, f"{video_id}.m4a")

    # Skip if already downloaded
    if os.path.exists(output_path):
        print(f"Audio already exists for {video_id}")
        return output_path

    command = [
        "yt-dlp",
        "-f", "bestaudio[ext=m4a]",
        "-o", output_path,
        video_url
    ]

    print(f"Downloading audio for {video_id}...")
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    if result.returncode != 0:
        raise RuntimeError(f"Failed to download audio:\n{result.stderr.decode()}")

    return output_path
