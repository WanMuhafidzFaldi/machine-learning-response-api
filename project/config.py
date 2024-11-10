import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    MONGO_URI = os.getenv("MONGO_URI")  # Gets the MongoDB connection URI from env
    MONGO_DATABASE_NAME = os.getenv("MONGO_DATABASE_NAME")  # We added this for clarity, although not directly used here