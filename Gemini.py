# LIbraries
from google import genai
from google.genai import types
from IPython.display import Markdown, display, HTML
from dotenv import load_dotenv
import os

#Loading API Key
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model="gemini-2.5-flash", contents="Tell me how an LLM model works like a kid"
)
print(response.text)