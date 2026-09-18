import os
from anthropic import Anthropic
from dotenv import load_dotenv
from pathlib import Path

load_dotenv(Path(__file__).parent / ".env")

client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

# A long system prompt — simulating a large document
# In real use this would be a full transcript or document
LONG_SYSTEM_PROMPT = """You are an expert Python tutor analyzing 
a YouTube tutorial transcript. Your job is to extract specific 
information from the transcript accurately and concisely.

TRANSCRIPT:
""" + ("Python is a versatile programming language. " * 150)
# Repeating to simulate a long transcript — over 1024 tokens


# ============================================
# LAYER 1 — Without caching (baseline)
# ============================================

def ask_without_cache(question:str)-> dict:
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        system=LONG_SYSTEM_PROMPT,
        messages=[{"role":"user", "content": question}]
    )

    return {
        "response": response.content[0].text,
        "input_tokens": response.usage.input_tokens,
        "output_tokens": response.usage.output_tokens
    }


# ============================================
# LAYER 2 — With prompt caching
# ============================================


def ask_with_cache(question:str)-> dict:
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        system=[
            {
                "type": "text",
                "text" : LONG_SYSTEM_PROMPT,
                "cache_control":{"type":"ephemeral"}
            }
        ],
        messages=[{"role":"user","content": question}]
    )

    #cache specific usage
    cache_created = getattr(response.usage,"cache_creation_input_tokens",0)
    cache_read = getattr(response.usage,"cache_read_input_tokens",0)

    return {
        "response": response.content[0].text,
        "input_tokens": response.usage.input_tokens,
        "output_tokens": response.usage.output_tokens,
        "cache_created": cache_created,
        "cache_read": cache_read
    }



if __name__ == "__main__":
    questions = [
        "What programming language is discussed?",
        "What are the key features mentioned?",
        "Summarize the main topic in one sentence."
    ]

    print("=== WITHOUT CACHING==")
    total_input = 0
    for q in questions:
        result = ask_without_cache(q)
        total_input += result['input_tokens']
        print(f"Q: {q}")
        print(f"Input tokens: {result['input_tokens']}")
        print()
    print(f"Total input tokens: {total_input}\n")

    print("=== WITH CACHING ===")
    total_input = 0
    for q in questions:
        result = ask_with_cache(q)
        total_input += result["input_tokens"]
        print(f"Q: {q}")
        print(f"Input tokens:  {result['input_tokens']}")
        print(f"Cache created: {result['cache_created']}")
        print(f"Cache read:    {result['cache_read']}")
        print()
    print(f"Total input tokens: {total_input}")

