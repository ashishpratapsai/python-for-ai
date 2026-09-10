import json

# 1. dict to JSON string

student = {
    "name":"Rahul Sharma",
    "marks":85,
    "passed": True,
    "subject": ["Physics","Maths","Chemistry"]

}

json_string = json.dumps(student, indent=2)
print(json_string)
print(type(json_string))

# 2. JSON string back to dict

data = json.loads(json_string)
print(data["name"])
print(data["subject"][0])


# 3. write JSON file

with open("students.json","w") as f:
    json.dump(student, f, indent=2)
print("Saved to student.json")

# 4. Read from JSON file

with open("students.json","r") as f:
    loaded =json.load(f)
print(loaded["name"])
print(loaded["marks"])

# writting he function that save student in json format


students = [
    {"name": "Rahul Sharma", "batch": "IIT-JEE-2026", "marks": 85, "fee_status": "paid"},
    {"name": "Priya Patel", "batch": "NEET-2026", "marks": 92, "fee_status": "paid"},
    {"name": "Amit Kumar", "batch": "IIT-JEE-2026", "marks": 0, "fee_status": "pending"},
]

def save_student_json(students:list[dict], filename:str)->None:
    with open(filename,"w") as f:
        json.dump(students, f, indent=2)
    return f"Saved to {filename} "

save_student_json(students, "list_of_students.json")
print("saved")

def load_students_json(filename: str) -> list[dict]:
    with open(filename,"r") as f:
        loaded = json.load(f)
    return loaded

loaded =load_students_json("list_of_students.json")
print(f"loaded {len(loaded)} students")
print(loaded)
for student in loaded:
    print(student["name"],"|", student["marks"])

#------------------
api_response = {
    "id": "msg_123",
    "type": "message",
    "role": "assistant",
    "content": [
        {
            "type": "text",
            "text": "Hello! How can I help you?"
        }
    ],
    "model": "claude-sonnet-4-6",
    "usage": {
        "input_tokens": 10,
        "output_tokens": 15
    }
}

def extract_response(api_response:dict)-> dict:
    
    return {
        "text":api_response["content"][0]["text"],
        "model":api_response["model"],
        "input_tokens":api_response["usage"]["input_tokens"],
        "output_tokens":api_response["usage"]["output_tokens"],
        "total_tokens":api_response["usage"]["input_tokens"] + api_response["usage"]["output_tokens"]

    }

print(extract_response(api_response))