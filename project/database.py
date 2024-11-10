from pymongo import MongoClient
from flask import current_app

# This function should only be called when the app context is active.
def get_db():
    client = MongoClient(current_app.config["MONGO_URI"])
    # Specify your database name here
    db_name = current_app.config["MONGO_DATABASE_NAME"] 
    db = client[db_name]
    return db

def check_connection():
    try:
        client = MongoClient(current_app.config["MONGO_URI"])
        # Replace this with your actual database name or fetch it from the .env file
        db_name = current_app.config["MONGO_DATABASE_NAME"] 
        # Attempt to ping the database
        client.admin.command('ping')  # This will ping the database
        # You could also check if a specific collection exists as an additional check
        # e.g., client[db_name].list_collection_names()
        return True  # Connection successful
    except Exception as e:
        # Log the type of exception and its details
        print(f"Database connection failed: {e}")  # Make sure to log/print the exception
        return False  # Connection failed