# tests/test_transcriber.py

import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from youtube.transcriber import transcribe
from config import AUDIO_DIR

video_id = "6BfEEwrHJH4"
audio_path = os.path.join(AUDIO_DIR, f"{video_id}.m4a")

if __name__ == "__main__":
    transcript = transcribe(audio_path, video_id)
    print("📝 Transcript snippet:")
    print(transcript[:500] + "..." if len(transcript) > 500 else transcript)
