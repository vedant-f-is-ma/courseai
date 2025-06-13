from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(), override=True)

from openai import OpenAI
client = OpenAI()

stream = client.chat.completions.create(
    model='gpt-4o-mini',
    messages=[
        {'role': 'developer', 'content': 'You high-school tutor.'},
        {'role': 'user', 'content': 'Explain Quantum Mechanics to teenagers.'}
    ],
    stream=True
)
print('AI is typing')
for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end='')
    