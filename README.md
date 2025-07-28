# CryptoInsightFlow

CryptoInsightFlow is a modular workflow that supports long-term crypto portfolio strategy by combining insights from YouTube content with live exchange data. Designed for periodic evaluation rather than real-time trading, it helps surface actionable, research-informed allocation suggestions.

Key Workflow Components
 - Monitors crypto-focused YouTube channels for new video uploads
 - Downloads and transcribes videos using yt-dlp and Whisper
 - Summarizes video content using large language models (e.g., GPT-4)
 - Fetches live portfolio allocations via exchange APIs (ccxt)
 - Runs scheduled evaluations that combine content and holdings
 - Suggests long-term allocation adjustments based on current insights via email

Technology Stack

LangChain – Orchestrates tools and reasoning flow
OpenAI (GPT-4) – Handles summarization and strategic reasoning
Whisper + yt-dlp – For automated video transcription
ccxt – Connects to major crypto exchanges for portfolio data
APScheduler – Schedules periodic portfolio reviews and updates
