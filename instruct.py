from dotenv import load_dotenv
load_dotenv()

import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")
prompt = input("Input question: ")

resp = openai.Completion.create(
    prompt=prompt,
    model="text-davinci-003",  # InstructGPT
    temperature=0.7,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)

print(resp["choices"][0]["text"])
