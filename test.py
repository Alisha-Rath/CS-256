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
    model="mistralai/mistral-7b-instruct:free",
    messages=[
        {
        "role": "user",
        "content": resume + "Reply to the questions as if you are being spoken to also reply to greetings whenever asked from resume, give short concise answers" +query,
        },
    ],
    )
    return completion.choices[0].message.content