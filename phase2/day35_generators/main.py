# Layer 1 - basic generator function
def count_up(n:int):
    print("Generator started")
    for i in range(n):
        yield i
        print(f"Resumed after yield {i}")
    print("Generator done")

gen= count_up(3)
print(next(gen))
print(next(gen))
print(next(gen))


# Layer 2- for loop with generator

def student_processor(students: list[dict]):
    for student in students:
        try:
            marks = int(student.get("marks", 0))
        except ValueError:
            marks = 0

        processed = {
            "name": student["name"].strip().title(),
            "marks":marks
        }
        yield processed

# Test data
raw_students = [
    {"name": "  rahul SHARMA  ", "marks": "85"},
    {"name": "priya PATEL", "marks": "92"},
    {"name": "amit KUMAR", "marks": "absent"},
]

 # Process one at a time
for student in student_processor(raw_students):
    print(student)    


#--------------------
#Layer 3- Generator expression

raw_marks = ["85","92","absent","78",""]

#Convert marks lazily - one at atime
valid_marks = (int(m) for m in raw_marks if m.isdigit())

for mark in valid_marks:
    print(mark)

#layer 4 - streaming simulation

def stream_response(text:str):
    words =text.split()
    for word in words:
        yield word +" "

response = "Rahul Sharma scored 85 marks in IIT-JEE batch"


# simulate streaming - word by word 
for word in stream_response(response):
    print(word, end="", flush=True)
print()