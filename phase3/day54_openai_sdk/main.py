import os
from openai import OpenAI
from anthropic import Anthropic
from dotenv import load_dotenv
from pathlib import Path

load_dotenv(Path(__file__).parent/".env")

openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
anthropic_client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))



# ============================================
# LAYER 1 — OpenAI basic call
# ============================================

def ask_openai(question:str)->str:
    response = openai_client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"user", "content": question}]
    )
    return response.choices[0].message.content

# ============================================
# LAYER 2 — Anthropic basic call (same pattern)
# ============================================
def ask_anthropic(question: str) -> str:
    response = anthropic_client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        messages=[{"role": "user", "content": question}]
    )
    return response.content[0].text


# ============================================
# LAYER 3 — Model abstraction
# ============================================

def ask_model(question:str, provider:str= "anthropic")->str:
    if provider=="openai":
        return ask_openai(question)
    elif provider == "anthropic":
        return ask_anthropic(question)
    else:
        raise ValueError(f"Unknown provider: {provider}")


if __name__=="__main__":
    question = "What is Python?Answer in one sentence"

    print("=== OPENAI ===")
    print(ask_openai(question))
    print()

    print("=== ANTHROPIC ===")
    print(ask_anthropic(question))
    print()

    print("=== MODEL ABSTRACTION ===")
    print(ask_model(question, provider="openai"))
    print(ask_model(question, provider="anthropic"))

