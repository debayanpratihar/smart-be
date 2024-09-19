from dotenv import load_dotenv
import os

load_dotenv()

SERVER_URL = '0.0.0.0'  # Bind to all interfaces for deployment
PORT = os.getenv('PORT', '8900')  # Use the PORT environment variable or default to 8900
ENV = 'dev'

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
