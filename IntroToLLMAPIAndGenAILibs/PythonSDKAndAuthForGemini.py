from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(), override=True)

import google.generativeai as genai
import os

genai.configure(api_key=os.environ.get('GOOGLE_API_KEY'))
for model in genai.list_models():
    print(model.name)