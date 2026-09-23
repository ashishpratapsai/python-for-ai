import os
from anthropic import Anthropic
from dotenv import load_dotenv
from pathlib import Path
from models import Student

load_dotenv(Path(__file__).parent/".env")

client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

def generate_summaries(students: list[Student])-> str:
    requests= []

    for s in students:
        requests.append({
            "custom_id": s.name.lower().replace(' ', '-'),
            "params":{
                "model":"claude-sonnet-4-6",
                "max_tokens": 1024,
                "messages":[{
                    "role":"user",
                    "content": f"write a parent summary for {s.name} "
                               f"who scored {s.marks}/100 in {s.batch} "
                               f"Fee status: {s.fee_status} "
                               f"If the marks of the students are 75+, then write in an encouraging tone. If the marks are between 40 and 74, the tone should be constructive. If the marks are below 40, the tone should be urgent. If the fee is pending, then add a fee reminder. "

                }]
            }
        })
    batch = client.messages.batches.create(requests=requests)
    return batch.id


def get_results(batch_id:str)-> dict |None:
    batch = client.messages.batches.retrieve(batch_id)
    print(f"Status: {batch.processing_status}")

    if batch.processing_status != "ended":
        print("batch not ready yet.")
        return None

    results= {}
    for result in client.messages.batches.results(batch_id):
        if result.result.type =="succeeded":
            results[result.custom_id] = result.result.message.content[0].text

        else:
            print(f"Failed: {result.custom_id}")
            results[result.custom_id] = "Error generating summary"

    return results

