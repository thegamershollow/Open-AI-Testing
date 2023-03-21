import os
import datetime
import openai

#get the current date and time for the GPT output file

CurrentTime = datetime.datetime.now()
Time = (CurrentTime.strftime("%H:%M:%S"))

#imliments an OpenAI api key from api.txt (you need to create this file)

api_call = open('api.txt')
api = api_call.read()
openai.api_key = api

#impliments chatgpt and passes a question to the model

question = input("Question for ChatGPT: ")
response = openai.ChatCompletion.create(
model="gpt-3.5-turbo",
messages=[{"role": "user", "content": question}]
)

#prints chatGPT's response to the terminal

print ('ChatGPT:', response['choices'][0]['message']['content'])

#writes chatGPT's response to an output file for analysis purposes

output = response['choices'][0]['message']['content']
file = open('output.txt', 'a') 
file.write('Prompt:')
file.write(question)
file.write('\nChatGPT:')
file.write(Time)
file.write('\n')
newOutput = output.replace("\n", "")
file.write(newOutput)
file.write('\n')
file.close
