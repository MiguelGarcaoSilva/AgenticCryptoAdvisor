# AgenticCryptoAdvisor

This project explores the use of AI agents for long-term crypto portfolio guidance and strategic decision support. It combines YouTube intelligence with live exchange portfolio data to act as a lightweight AI financial assistant — focused on periodic evaluation, not real-time trading signals.

Main Features

- Monitors selected crypto YouTube channels for new video uploads
- Transcribes and summarizes video content using Whisper and LLMs (e.g., GPT-4)
- Connects to exchanges (via ccxt) to fetch live portfolio allocations
- Uses a LangChain agent to reason over video insights and current holdings
- Suggests long-term allocation changes and optionally notifies the user via email

Tech Stack

LangChain agents – Tool orchestration and reasoning loop
OpenAI (GPT-4) – Summarization and decision-making logic
yt-dlp + Whisper – Video downloading and transcription
ccxt – Unified API access to crypto exchanges (e.g., Binance)
APScheduler – Scheduled portfolio and content evaluations
