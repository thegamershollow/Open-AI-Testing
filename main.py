import os
import openai
openai.organization = "org-C69lk72lYbzrRrBifeRKi6l4"
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.Model.list()