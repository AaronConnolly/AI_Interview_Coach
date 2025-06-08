import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load the API key from .env
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# list models
#models = genai.list_models()
#for model in models:
#    print(model.name, model.supported_generation_methods)

# Basic Gemini call
model = genai.GenerativeModel("models/gemini-1.5-flash-latest")
response = model.generate_content("What is the capital of Ireland?")
print(response.text)
