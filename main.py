import os
import openai
api_call = open('api.txt')
api = api_call.read()
openai.api_key = api

question = input("Question for ChatGPT:")
openai.ChatCompletion.create(
model="gpt-3.5-turbo",
messages=[
    {"role": "user", "content": question}
    ]
)