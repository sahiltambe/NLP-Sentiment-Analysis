import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    MODEL_NAME = "llama-3.1-8b-instant"  # Updated to supported model
    MAX_TOKENS = 150
    TEMPERATURE = 0.1