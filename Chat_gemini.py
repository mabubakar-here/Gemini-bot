## Gemini working api with chat history


#Loading libraries
from google import genai
from google.genai import types
from IPython.display import Markdown, HTML, display
from dotenv import load_dotenv
import os


#loading api key
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
client= genai.Client(api_key=api_key)


