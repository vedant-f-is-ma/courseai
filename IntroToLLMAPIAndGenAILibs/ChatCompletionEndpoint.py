from openai import OpenAI
from dotenv import load_dotenv, find_dotenv
import os

# Load environment variables
load_dotenv(find_dotenv(), override=True)
api_key = os.getenv('OPENAI_API_KEY')

client = OpenAI(api_key=api_key)
response = client.chat.completions.create(
    model='gpt-4',
    messages=[
        {'role': 'system', 'content': 'You are a Sci-Fi writer and poet.'},
        {'role': 'user', 'content': 'Write a poem about a lonely robot exploring a futuristic city.'}
    ],
    temperature=1
)

print(response.choices[0].message.content)