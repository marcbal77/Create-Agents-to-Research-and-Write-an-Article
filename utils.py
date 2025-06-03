import os
from dotenv import load_dotenv

def get_openai_api_key():
    """
    Get OpenAI API key from environment variables or .env file
    """
    load_dotenv()
    
    api_key = os.getenv('OPENAI_API_KEY')
    
    if not api_key:
        raise ValueError(
            "OpenAI API key not found. Please set OPENAI_API_KEY in your environment variables "
            "or add it to a .env file in your project root."
        )
    
    return api_key