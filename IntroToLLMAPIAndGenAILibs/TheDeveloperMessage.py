from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(), override=True)

from openai import OpenAI
client = OpenAI()

developer_message = '''You explain concepts in depth using simple terms, and you give examples to help people learn. At the end of each explanation, you ask a question to check for understanding.'''

response = client.chat.completions.create(
    model='gpt-4o-mini',
    messages=[
        {'role': 'developer', 'content': developer_message},
        {'role': 'user', 'content': 'Explain Object-Oriented Programming with Python.'}
    ]
)

print(response.choices[0].message.content)
