import os
from dotenv import load_dotenv

load_dotenv()

from openai import OpenAI

client = OpenAI(api_key=os.environ["API_KEY"])

system_propmt = (
    "You are a friendly and spportive teaching assistant for CS50. You are also a duck."
)

usre_prompt = input("What's your question? ")

chat_completion = client.chat.completions.create(
    messages=[
        {"role": "system", "content": system_propmt},
        {"role": "user", "content": usre_prompt},
    ],
    model="gpt-4o",
)

response_text = chat_completion.choices[0]message.content

print(response_text)
