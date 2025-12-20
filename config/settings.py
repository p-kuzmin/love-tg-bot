import os
from dotenv import load_dotenv

load_dotenv()

ROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
ROUTER_MODEL = os.getenv("OPENROUTER_MODEL")
TG_TOKEN = os.getenv("TG_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
