import os
from dotenv import load_dotenv

load_dotenv()

ROUTER_API_KEY = os.getenv("ROUTER_API_KEY")
ROUTER_MODEL = os.getenv("ROUTER_MODEL")
TG_TOKEN = os.getenv("TG_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
