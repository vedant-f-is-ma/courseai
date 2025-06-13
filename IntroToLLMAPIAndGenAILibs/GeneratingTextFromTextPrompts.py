from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(), override=True)

import google.generativeai as genai
import os

model = genai.GenerativeModel('gemini-1.5-flash')
response = model.generate_content('Explain the concept of Quantum Mechanics to a 10 year old')
print(response)

model_info = genai.get_model('models/gemini-1.5-flash')
print(model_info)