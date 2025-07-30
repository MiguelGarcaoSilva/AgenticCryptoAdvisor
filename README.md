# CryptoInsightFlow

**CryptoInsightFlow** is a modular workflow designed to support long-term cryptocurrency portfolio management by combining insights from crypto-focused YouTube content with live exchange data. It is intended for periodic evaluations, not real-time trading, and helps surface actionable, research-driven allocation suggestions.

---

## Key Workflow Components

- **YouTube Channel Monitoring**  
  Monitors specified crypto-focused YouTube channels for new uploads using RSS feeds. Scheduled polling is managed with APScheduler (default interval: every 1 minute).

- **Audio Download and Transcription**  
  Downloads audio using `yt-dlp` and transcribes it using a speech-to-text model (e.g., OpenAI Whisper running locally).

- **Content Summarization**  
  Uses large language models (LLMs) such as GPT-4 or local alternatives (e.g., Mistral, LLaMA) to summarize the transcribed content into structured insights.

- **Portfolio Retrieval**  
  Connects to supported cryptocurrency exchanges via the `ccxt` library to retrieve the user’s current portfolio allocations using read-only API keys.

- **Insight Evaluation and Strategy Recommendation**  
  Compares extracted insights with current holdings to identify misalignments or opportunities. Generates high-level strategic suggestions for portfolio adjustment.

- **Email Notifications**  
  If the evaluation identifies a significant actionable insight, an allocation recommendation is emailed to the user.

---

## Technology Stack

Youtube RSS feeds, APscheduler - Video Monitoring 
Whisper + yt-dlp – For automated audio downloading and transcription
ccxt – Connects to crypto exchanges for portfolio data
Local Open-Source LLMs – Handles summarization and strategic reasoning