import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY') or os.urandom(32).hex()  # Fallback if not in .env
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI') or 'sqlite:///secure_app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    RATELIMIT_DEFAULT = "200 per day;50 per hour"  # Global rate limit