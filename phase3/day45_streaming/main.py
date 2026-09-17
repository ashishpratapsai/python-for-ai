import os
from anthropic import Anthropic
from dotenv import load_dotenv
from pathlib import Path

load_dotenv(Path(__file__).parent/".env")

client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

#--------
#Layer 1 - basic streaming
#-------------

def stream_response(question:str, system:str ="")-> None:
    print("claude: ", end="", flush=True)

    with client.messages.stream(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        system=system,
        messages=[{"role": "user","content": question}]
    ) as stream:
        for text in stream.text_stream:
            print(text, end="", flush=True)

    print() # a new line afer response


if __name__ =="__main__":
    stream_response(
        question= "write a short poem about Python programing.",
        system="You are a creative writer"
    )

#==========
#Layer 2 - streming with conversation history
#===========


def stream_chat(system: str="")->None:
    conversation_history = []

    print("Streaming chat started. Type 'quit' to exit.\n")

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() == "quit":
            print("Chat ended.")
            break
        if not user_input:
            continue

        conversation_history.append({
            "role": "user",
            "content": user_input

        })

        print("Claude: ", end="", flush=True)
        full_response =""

        with client.messages.stream(
            model="claude-sonnet-4-6",
            max_tokens=1024,
            system=system,
            messages=conversation_history
        ) as stream:
            for text in stream.text_stream:
                print(text, end="", flush=True)
                full_response += text #collect full response

        print()

        # Add complete response to history
        conversation_history.append({
            "role": "assistant",
            "content": full_response
        })

if __name__=="__main__":
    stream_chat(system="You are a helpful Python tutor. Keep answer short")