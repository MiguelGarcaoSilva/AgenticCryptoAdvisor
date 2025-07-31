# summarization/summarizer.py

import os
import time
import requests
from config import HF_API_TOKEN, TRANSCRIPTS_DIR

API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"

HEADERS = {
    "Authorization": f"Bearer {HF_API_TOKEN}",
    "Content-Type": "application/json"
}

def load_transcript(video_id: str) -> str:
    path = os.path.join(TRANSCRIPTS_DIR, f"{video_id}.txt")
    if not os.path.exists(path):
        raise FileNotFoundError(f"Transcript not found: {path}")
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def build_prompt(transcript: str) -> str:
    return f"""
You are a crypto-focused transcription analyst.

Your task is to take a raw transcript of a spoken video and convert it into a clear, highly detailed, structured text format. Your goal is to preserve all important facts, opinions, and reasoning from the original speaker while eliminating irrelevant filler language, conversational noise, and informalities.

Instructions:
1. Do not summarize. Restate the full content in cleaned, formal written form.
2. Preserve all details, including token mentions, price targets, and predictions.
3. Remove greetings, jokes, tangents, and filler language.
4. Use sections and bullet points to organize the content.
5. The output should be suitable for further analysis by a reasoning model.

Transcript:
{transcript}
"""

def summarize_transcript(video_id: str, max_retries: int = 3) -> str:
    transcript = load_transcript(video_id)
    prompt = build_prompt(transcript)

    for attempt in range(max_retries):
        try:
            response = requests.post(
                API_URL,
                headers=HEADERS,
                json={
                    "inputs": prompt,
                    "parameters": {
                        "max_new_tokens": 1024,
                        "temperature": 0.5
                    }
                },
                timeout=60
            )

            if response.status_code in [401, 403]:
                raise RuntimeError(
                    f"Authentication error. Please check your HF_API_TOKEN. "
                    f"Status: {response.status_code}"
                )

            if response.status_code == 404:
                raise RuntimeError(f"Model not found. Check API_URL: {API_URL}")

            if response.status_code != 200:
                raise RuntimeError(f"API error {response.status_code}: {response.text}")

            result = response.json()

            # Parse standard inference response
            if isinstance(result, list) and "generated_text" in result[0]:
                return result[0]["generated_text"]
            elif isinstance(result, dict) and "generated_text" in result:
                return result["generated_text"]

            raise ValueError("Unexpected response format")

        except (requests.RequestException, ValueError) as e:
            if attempt == max_retries - 1:
                raise
            time.sleep(2 ** attempt)

    raise RuntimeError("Maximum retries reached")
