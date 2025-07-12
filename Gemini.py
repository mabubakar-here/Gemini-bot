## With the help of this code we can generate one time response form gemini but gemini cannot remeber previous message

# LIbraries
from google import genai
from google.genai import types
from IPython.display import Markdown, display, HTML
from dotenv import load_dotenv
import os

#Loading API Key and generating response
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model="gemini-2.5-flash", contents="Tell me how an LLM model works like a kid"
)
Markdown(response.text) #Markdown is used to decorate the response i.e. bold 


