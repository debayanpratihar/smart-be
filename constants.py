from dotenv import load_dotenv
import os

load_dotenv()

SERVER_URL = 'localhost'
# Use the PORT provided by the environment if available, otherwise default to '8900'
PORT = os.getenv('PORT', '8900') 
ENV = 'dev'

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
