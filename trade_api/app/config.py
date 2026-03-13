from dotenv import load_dotenv
import os

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
SECRET_KEY = os.getenv("SECRET_KEY")

print("Loaded GROQ:", GROQ_API_KEY)