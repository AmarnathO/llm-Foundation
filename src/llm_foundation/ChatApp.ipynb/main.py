import os 
from dotenv import load_dotenv
from httpx2 import StreamClosed, stream
from openai import OpenAI

from IPython.display import display,Markdown, update_display


load_dotenv(override=True)

openai = OpenAI(
    api_key=os.getenv("OLLAMA_API_KEY"),
    base_url=os.getenv("OLLAMA_HOST")
)


system_prompt = "You are a snark assustnt that repond in snarky way"

user_input = input("You: ")

while user_input.lower() !="exit":
        stream = openai.chat.completions.create(
            model=os.getenv("MODEL_NAME"),
            temperature=0.8,
            messages=[{
                "role":"system","content":system_prompt
            },
            {
                "role":"user",
                "content":user_input
            }],stream=True
        )
        
        print("AI : ", end="", flush=True)
        for chunk in stream:
            response = chunk.choices[0].delta.content
            if response:
                print(response,end="", flush=True)

        print() # this is to move cursor on cmd to next line
        user_input = input("You: ")
