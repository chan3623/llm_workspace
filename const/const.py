import os

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("NVIDIA")
MODEL = os.getenv("NVIDIA_MODEL")
EMBEDDING_MODEL = os.getenv("NVIDIA_EMBEDDING")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
