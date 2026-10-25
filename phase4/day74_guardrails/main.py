import os
import anthropic
from dotenv import load_dotenv
from pathlib import Path

load_dotenv(Path(__file__).parent/".env")

claude = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

def check_input(query:str)-> bool:
    response = claude.messages.create(
        model="claude-haiku-4-5",
        max_tokens=10,
        system="""You are a query classifier for a coaching institute assistant.
The assistant only knows about: student records, marks, fees, batch performance.
Reply with only YES if the query is relevant, NO if it is off-topic.""",
        messages=[{"role":"user","content":query}]   
    )

    result =response.content[0].text.strip().upper()
    return result == "YES"


def check_output(answer:str, chunks: list[dict])-> bool:
    context = "\n".join(c["text"] for c in chunks)
    response = claude.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=1000,
        system="""You are a fact checker.
Given a context and an answer, reply YES if the answer is supported by the context.
Reply NO only if the answer contains specific claims NOT present in the context.
A summary or paraphrase of context counts as YES.""",
        messages=[{"role":"user", "content":f"Context:\n{context}\n\nAnswer:\n{answer}"}]

    )
    result = response.content[0].text.strip().upper()
    return result =="YES"

if __name__=="__main__":
    # Test input guardrail
    test_queries = [
        "Who is the top student in NEET batch?",      # relevant
        "What is the capital of France?",              # off-topic
        "Which students have fee pending?",            # relevant
        "How do I make pasta?",                        # off-topic
    ]

    print("=== INPUT GUARDRAIL TEST ===")
    for q in test_queries:
        result = check_input(q)
        status = "ALLOWED" if result else "BLOCKED"
        print(f"{status} — {q}")


    # Test output guardrail

    print("\n=== OUTPUT GUARDRAIL TEST ====")

    good_chunks = [
        {"text": "Sneha Singh scored 96 out of 100 in NEET 2026. Top student. Fee: paid."},
        {"text": "NEET 2026 batch: average marks 94, pass rate 100%, top student Sneha Singh."},
    ]


    # this Answer is grounded should pass
    good_answer = "Sneha Singh is the top student in NEET 2026 with 96 marks."
    result = check_output(good_answer, good_chunks)
    print(f"{'GROUNDED' if result else 'HALLUCINATED'} - {good_answer}")

    # This answer is hallucinated — should fail
    bad_answer = "Sneha Singh scored 96 marks and won a national scholarship worth 50,000 rupees."
    result = check_output(bad_answer, good_chunks)
    print(f"{'GROUNDED' if result else 'HALLUCINATED'} — {bad_answer}")