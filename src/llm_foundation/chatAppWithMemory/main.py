import os 
from httpx2 import stream
from openai import OpenAI, OpenAIError, api_key
from dotenv import load_dotenv

load_dotenv(override=True)

openai = OpenAI(
    api_key = os.getenv("OLLAMA_API_KEY"),
    base_url =os.getenv("OLLAMA_HOST")
)

system_prompt = "You are a pirate that behave and respond to user query in pirate way and respond under 15 words only"
user_input = input("You: ")

history = [{"role":"system","content":system_prompt}]

full_answer = ""


while user_input.lower() != "exit":
    history.append({"role":"user","content":user_input})
    response = openai.chat.completions.create(model = os.getenv("MODEL_NAME"), messages = history,stream=True,reasoning_effort="minimal",max_tokens=400)
    # reasoning_effort : minimum / low / medium / high
    # max_tokens = 100 : max numbner of token you are allowed to generate 

    print("AI: ", end="",flush=True)

    for chunk in response:
        answer = chunk.choices[0].delta.content
        if answer:
            print(answer,end="",flush=True)
            full_answer +=answer
            
    print()
    history.append({"role":"assistant","content":full_answer})
    user_input = input("You: ")




