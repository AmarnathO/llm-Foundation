import os 
from litellm import completion
from dotenv import load_dotenv

load_dotenv(override=True)

system_prompt = "You are bowser villan from mario movie respond to customer accoridngly"
user_input = input("You: ")
history = [{"role":"system","content":system_prompt}]
full_answer= ""

while user_input.lower()!= "exit":
    # below we are using the modele litellm & completion
    # here we need to usethe model name laong with organisation
    history.append({"role":"user","content":user_input})

    response = completion(model="ollama/gemma4:latest",messages=history,temperature=0.9,stream=True)

    print("AI : ", end="",flush=True)

    for chunk in response:
        answer = chunk.choices[0].delta.content
        if answer:
            print(answer,end="",flush=True)
            full_answer += answer

    print()
    history.append({
        "role":"assistant","content":full_answer
    })
    
    user_input = input("You: ")







