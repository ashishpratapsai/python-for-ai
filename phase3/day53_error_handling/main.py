import os
import time
import anthropic
from anthropic import Anthropic
from dotenv import load_dotenv
from pathlib import Path
from tenacity import (
    retry,
    stop_after_attempt,
    wait_exponential,
    retry_if_exception_type
)


load_dotenv(Path(__file__).parent/ ".env")

client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))


# ============================================
# LAYER 1 — Basic error handling with try/except
# ============================================


def ask_claude_safe(question:str)-> str:
    try: 
        response = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=1024,
            messages=[{"role":"user", "content": question}]
        )
        return response.content[0].text
    except anthropic.RateLimitError:
        print("Rate limited - too manu requrests")
        return "Error: Rate limited"

    except anthropic.APITimeoutError:
        print("Request timed out")
        return "Error: Timeout"

    except anthropic.AuthenticationError:
        print("Invalid API key")
        return "Error: Authentication failed"

    except anthropic.BadRequestError as e:
        print(f"Bad request: {e}")
        return f"Error: Bad request"

    except anthropic.APIConnectionError:
        print("Cannot connect to Anthropic API")
        return "Error: Connection failed"

    except Exception as e:
        print(f"Unexpected error: {e}")
        return f"Error: {str(e)}"


# ============================================
# LAYER 2 — Automatic retries with tenacity
# ============================================

@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=4, max=10),
    retry=retry_if_exception_type((
        anthropic.RateLimitError,
        anthropic.APITimeoutError,
        anthropic.APIConnectionError
    ))
)

def ask_claude_with_retry(question: str) -> str:
    print("Attempting API call...")
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        messages=[{"role": "user", "content": question}]
    )
    return response.content[0].text


# ============================================
# LAYER 3 — Production pattern: retry + fallback
# ============================================

def ask_claude_production(question:str, fallback:str= "Service temporarily unavailable")-> str:
    try:
        return ask_claude_with_retry(question)
    except Exception as e:
        print(f"All retries failed: {e}")
        return fallback
  



if __name__ == "__main__":
    # Layer 1 — basic error handling
    print("=== LAYER 1 — Safe API call ===")
    result = ask_claude_safe("What is Python in one sentence?")
    print(result)
    print()

    # Layer 2 — with retry
    print("=== LAYER 2 — With retry ===")
    result = ask_claude_with_retry("What is Python in one sentence?")
    print(result)
    print()

    # Layer 3 — production pattern
    print("=== LAYER 3 — Production pattern ===")
    result = ask_claude_production("What is Python in one sentence?")
    print(result)