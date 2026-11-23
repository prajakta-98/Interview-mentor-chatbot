import os 
from dotenv import load_dotenv

#Load environment variables from .env file
load_dotenv()

#Application configuration
MODEL_NAME = os.getenv("MODEL_NAME", "llama3.2")
OLLAMA_BASE_URL = os.getenv(
     "OLLAMA_BASE_URL",
     "http://localhost:11434"
     )
TEMPERATURE = float(os.getenv("TEMPERATURE", 0))