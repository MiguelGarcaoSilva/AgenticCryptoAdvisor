import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from summarization.summarizer import summarize_transcript

video_id = "6BfEEwrHJH4"

if __name__ == "__main__":
    summary = summarize_transcript(video_id)
    print("Generated Summary:\n")
    print(summary)
