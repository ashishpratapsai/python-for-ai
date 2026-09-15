import os
from anthropic import Anthropic
from dotenv import load_dotenv
from pathlib import Path

load_dotenv(Path(__file__).parent/".env")

client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
#===================
# Layer 1 - Basic Api call
#====================
def ask_claude(question:str)-> str:
    message = client.messages.create(
        model = "claude-sonnet-4-6",
        max_tokens = 1024,
        messages=[
            {"role": "user", "content": question}
        ]
    )
    return message.content[0].text

if __name__ =="__main__":
    response = ask_claude("What is python used for? Answer in 2 sencences.")
    print(response)



#================
# Layer 2 - with system prompt
#=================

def ask_claude(question:str, system: str="")-> str:
    message = client.messages.create(
        model= "claude-sonnet-4-6",
        max_tokens= 1024,
        system=system,
        messages= [
            {"role": "user", "content" :question}
        ]
    )
    return message.content[0].text

if __name__ == "__main__":
    #Without system prompt
    response = ask_claude("What is Python")
    print("WITHOUT SYSTEM:")
    print(response)
    print()


    #With system prompt

    response = ask_claude(
        question="What is Python?",
        system="You are aPython teacher for beginner in India.Always answer in English-Hindi mix. keep answer under 3 sentences "

    )
    print("WITH SYSTEM:")
    print(response)

#===============
# Layer 3 - Token Counting and cost tracking 
#===============

def ask_claude_with_usage(question:str, system:str="")->str:
    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens= 1024,
        system=system,
        messages=[
            {"role":"user", "content": question}
        ]

    )
    return{
        "response": message.content[0].text,
        "input_tokens": message.usage.input_tokens,
        "output_tokens": message.usage.output_tokens,
        "total_tokens": message.usage.input_tokens + message.usage.output_tokens
    }

if __name__ == "__main__":
    result = ask_claude_with_usage(
        question="What is Python? Answer in 2 sentences.",
        system="You are a helpful asssistant."
    )

    print(result["response"])
    print(f"\nToken Used:")
    print(f"Input: {result["input_tokens"]}")
    print(f"Output: {result["output_tokens"]}")
    print(f"Total: {result["total_tokens"]}")