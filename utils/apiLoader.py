import os
from dotenv import load_dotenv

def load_key():
    # Load environment variables from .env file
    load_dotenv()

    # Get environment variables
    api_key = os.getenv("ALI_API_KEY")

    # Check if environment variables are present
    if not api_key:
        raise ValueError("Environment variables \"ALI_API_KEY\" are missing.")

    # Return environment variables as dictionary
    return api_key