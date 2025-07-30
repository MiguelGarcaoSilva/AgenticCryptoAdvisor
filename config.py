import os
from dotenv import load_dotenv

# Load .env file automatically
load_dotenv()

# Base paths
DATA_DIR = "data"
SEEN_VIDEOS_PATH = os.path.join(DATA_DIR, "seen_videos.json")
CHANNELS_PATH = os.path.join(DATA_DIR, "channels.json")

# API Keys

