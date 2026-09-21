import os
import time
from anthropic import Anthropic
from dotenv import load_dotenv
from pathlib import Path

load_dotenv(Path(__file__).parent / ".env")

client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))


# ============================================
# LAYER 1 — Create a batch request
# ============================================

def create_batch(students:list[dict])-> str:
    requests=[]

    for student in students:
        requests.append({
            "custom_id":f"{student['name'].lower().replace(' ','-')}",
            "params":{
                "model":"claude-sonnet-4-6",
                "max_tokens": 1024,
                "messages":[{
                    "role": "user",
                    "content": f"write a short parent summary for {student['name']} "
                               f"who scored {student['marks']}/100 in {student['batch']}. "
                               f"Fee status: {student['fee_status']}. "
                               f"Keep it under 3 sentences, professional tone. "
                    
                }]
            }
        })
    batch = client.messages.batches.create(requests= requests)
    print(f"Batch created: {batch.id}")
    print(f"Status: {batch.processing_status}")
    print(f"Total requests: {len(requests)}")
    return batch.id


        

# ============================================
# LAYER 2 — Check batch status and get results
# ============================================

def get_batch_results(batch_id:str) ->dict:
    # Check current status
    batch = client.messages.batches.retrieve(batch_id)
    print(f"Status: {batch.processing_status}")
    print(f"Count: {batch.request_counts}")

    if batch.processing_status != "ended":
        print("Batch not ready yet. Check back later.")
        return {}

    # Get results
    results = {}
    for result in client.messages.batches.results(batch_id):
        custom_id = result.custom_id
        if result.result.type == "succeeded":
            results[custom_id] = result.result.message.content[0].text
        else:
            results[custom_id] =f"Error: {result.result.error}"

    return results


if __name__ == "__main__":
    # Sample students
    students = [
        {"name": "Rahul Sharma", "marks": 85, "batch": "IIT-JEE-2026", "fee_status": "paid"},
        {"name": "Priya Patel",  "marks": 92, "batch": "NEET-2026",    "fee_status": "paid"},
        {"name": "Amit Kumar",   "marks": 35, "batch": "IIT-JEE-2026", "fee_status": "pending"},
    ]

    #create Batch
    # print("=== CREATING BATCH ===")
    # batch_id = create_batch(students)

    # print(f"\n Batch ID:{batch_id}")
    # print("In production - save this ID and check result later")
    # print("For demo - wating 30 seconds and checking...")


    # # Wait and check
    # time.sleep(30)

    # print("\n=== GETTING RESULTS ===")
    # results = get_batch_results(batch_id)

    # for student_id, summary in results.items():
    #     print(f"\n{student_id}:")
    #     print(summary)

   # got the batch id in terminal then running this 
    batch_id = "msgbatch_01D9qGCfJB9kCq6Z7v1sxjnw"
    results = get_batch_results(batch_id)
    for student_id, summary in results.items():
        print(f"\n{student_id}:")
        print(summary)


