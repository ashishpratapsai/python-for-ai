import os
from anthropic import Anthropic
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(Path(__file__).parent/".env")

client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))


# Pricing for claude-sonnet-4-6
INPUT_COST_PER_MILLION = 3.00 #USD
OUTPUT_COST_PER_MILLION = 15.00 #USD
USD_TO_INR = 95

#================
# Layer 1 - Token counting per call
#================


def calculate_cost(input_tokens: int, output_tokens: int)-> dict:
    input_cost = (input_tokens/1_000_000)* INPUT_COST_PER_MILLION
    output_cost = (output_tokens/1_000_000)* OUTPUT_COST_PER_MILLION
    total_usd = input_cost + output_cost
    total_inr = total_usd * USD_TO_INR

    return {
        "input_tokens": input_tokens,
        "output_tokens": output_tokens,
        "total_tokens": input_tokens + output_tokens,
        "cost_usd": round(total_usd, 6),
        "cost_inr": round(total_inr, 4)
    }

def ask_with_cost(question:str, system:str="")-> dict:
    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        system=system,
        messages=[{"role":"user", "content": question}]
    )

    cost = calculate_cost(
        message.usage.input_tokens,
        message.usage.output_tokens
    )

    return {
        "response": message.content[0].text,
        "cost": cost
    }

# if __name__=="__main__":
#     result = ask_with_cost(
#         question="what is Python. Answer in 2 sentences.",
#         system= " You are a helpful assistant"
#     )
#     print(result["response"])
#     print(f"\nInput Tokens: {result['cost']['input_tokens']}")
#     print(f"Output Tokens: {result['cost']['output_tokens']}")
#     print(f"Cost USD: ${result['cost']['cost_usd']}")
#     print(f"Cost USD: ₹{result['cost']['cost_inr']}")


#=============
#layer 2 - Cost tracking Accross conversation
#=============

def chat_with_cost(system:str = "") -> None:
    conversation_history =[]
    total_input_tokens = 0
    total_output_tokens = 0

    print("Chat started. Type 'quit' to see total cost.\n")

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() == "quit":
            total_cost = calculate_cost(total_input_tokens,total_output_tokens)
            print("\n=== CONVERSATION COST SUMMARY ===")
            print(f"Total input tokens:  {total_cost['input_tokens']}")
            print(f"Total output tokens: {total_cost['output_tokens']}")
            print(f"Total tokens:        {total_cost['total_tokens']}")
            print(f"Total cost USD:      ${total_cost['cost_usd']}")
            print(f"Total cost INR:      ₹{total_cost['cost_inr']}")
            break

        if not user_input:
            continue

        conversation_history.append({
            "role":"user",
            "content":user_input
        })

        message = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=1024,
            system=system,
            messages=conversation_history
        )

        claude_response = message.content[0].text

        # track tokens per message
        input_tokens = message.usage.input_tokens
        output_tokens = message.usage.output_tokens
        total_input_tokens += input_tokens
        total_output_tokens += output_tokens

        msg_cost = calculate_cost(input_tokens,output_tokens)

        conversation_history.append({
            "role": "assistant",
            "content": claude_response
        })

        print(f"Claude: {claude_response}")
        print(f"[Tokens: {msg_cost['total_tokens']} | Cost: ₹{msg_cost['cost_inr']}]")

if __name__=="__main__":
    chat_with_cost(system="you are a helpful Python tutor. keep answers short.")



