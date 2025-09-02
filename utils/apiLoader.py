import os
from dotenv import load_dotenv

def load_item():
    # Load environment variables from .env file
    load_dotenv()

    # Get environment variables
    api_key = os.getenv("OPENAI_API_KEY")

    # Check if environment variables are present
    if not api_key:
        raise ValueError("Environment variables are missing.")

    # Return environment variables as dictionary
    return {
        "api_key": api_key
    }