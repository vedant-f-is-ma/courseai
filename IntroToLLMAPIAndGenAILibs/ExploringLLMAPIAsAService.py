from openai import OpenAI
from dotenv import load_dotenv, find_dotenv
import os


load_dotenv(find_dotenv(), override=True)
os.getenv('OPENAI_API_KEY')
client = OpenAI()

def ask_ai(prompt, temperature=1):
    completion = client.chat.completions.create(
        model='gpt-4o',
        messages=[
            {'role': 'system', 'content': 'You are a responder and you respond all of my questions with only one word yes and no with no periods'},
            {'role': 'user', 'content': prompt}
        ],
        temperature=temperature
    )
    return completion.choices[0].message.content
print(ask_ai('Whats up'))