from openai import OpenAI
from os import getenv
from key import key

# gets API Key from environment variable OPENAI_API_KEY
client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=key,
)

with open('resume.txt', 'r') as f:
    resume = f.read()

def get_response(query):
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo-instruct",
    messages=[
        {
        "role": "user",
        "content": resume + "You are an assitant created to make Alisha's life easier. Assume that role and respond to the following query: " +query,
        },
    ],
    )
    return completion.choices[0].message.content
