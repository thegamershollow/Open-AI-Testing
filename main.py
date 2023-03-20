import os
import openai
openai.organization = "org-C69lk72lYbzrRrBifeRKi6l4"
openai.api_key = os.getenv("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")
openai.Model.list()