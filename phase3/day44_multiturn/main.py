import os
from anthropic import Anthropic
from dotenv import load_dotenv
from pathlib import Path

load_dotenv(Path(__file__).parent/".env")

client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

#=============
# Layer 1- Multi-turn conversation
#=============

def chat(system:str="")-> None:
    conversation_history = [] # stores full conversation

    print("Chat started. Type 'quit' to exit.\n")

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() == "quit":
            print("Chat ended")
            break

        if not user_input:
            continue

        #Add user message to history
        conversation_history.append({
            "role": "user",
            "content": user_input
        })

        #send full history to claude 
        message = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=1024,
            system=system,
            messages= conversation_history
        )

        # get Claude's response
        claude_response = message.content[0].text

        #Add Claude's response to history

        conversation_history.append({
            "role":"assistant",
            "content":claude_response
        })

        print(f"Claude: {claude_response}\n")


# if __name__ =="__main__":
#     chat(system="you are a helpful python tutor. keep answer shor and clear.")



#=================
#Layer 2 - print conversation history
#================

def chat_with_history(system: str ="")-> None:
    conversation_history =[]

    print("Chat started.Type 'quit' to exit.\n")

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() =="quit":
            print("\n=== CONVERSATION HISTORY ===")
            for msg in conversation_history:
                role ="You" if msg["role"] =="user" else "Claude"
                print(f"{role}: {msg['content'][:50]}...")
            print(f"\nTotal message : {len(conversation_history)}")
            break

        if not user_input:
            continue

        conversation_history.append({
            "role":"user",
            "content": user_input
        })

        message = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=1024,
            system=system,
            messages=conversation_history
        )


        claude_response = message.content[0].text

        conversation_history.append({
            "role": "assistant",
            "content": claude_response

        })

        print(f"Claude: {claude_response}")

if __name__ == "__main__":
    chat_with_history(system="You are an helpful Python tutor. keep Your ans short.")