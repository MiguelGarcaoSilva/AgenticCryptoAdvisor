# youtube/transcriber.py

import whisper
import os
from config import TRANSCRIPTS_DIR

# Load the Whisper model (tiny/small/base/large)
model = whisper.load_model("tiny", device="cpu")

def transcribe(audio_path: str, video_id: str) -> str:
    os.makedirs(TRANSCRIPTS_DIR, exist_ok=True)
    transcript_path = os.path.join(TRANSCRIPTS_DIR, f"{video_id}.txt")

    if os.path.exists(transcript_path):
        print(f"⚠️ Transcript already exists for {video_id}")
        with open(transcript_path, "r") as f:
            return f.read()

    print(f"🧠 Transcribing {audio_path} locally with Whisper...")

    result = model.transcribe(audio_path)
    text = result["text"]

    with open(transcript_path, "w") as f:
        f.write(text)

    return text
