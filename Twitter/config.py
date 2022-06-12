import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    CONSUMER_KEY = os.getenv("API_KEY")
    CONSUMER_SECRET = os.getenv("API_KEY_SECRET")
    
    ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
    ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

    BEARER_TOKEN = os.getenv("BEARER_TOKEN")
