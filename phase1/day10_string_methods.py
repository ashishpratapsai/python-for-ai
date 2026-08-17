


# Institura real data

teacher_name = " mrs. priya sharma"
batch_code = "iit-jee-2026-morning"
subject = "PHYSICS"

print(teacher_name.strip())
print(teacher_name.strip().title())
print(batch_code.upper())
print(batch_code.replace("-"," ").title())
print(subject.lower())


student = {
    "name": "  rahul SHARMA  ",
    "batch": "iit-jee-2026-morning",
    "subject": "PHYSICS",
    "email": "  Rahul.Sharma@Gmail.COM  "
}

"""
{
    "name": "Rahul Sharma",        # stripped + title case
    "batch": "IIT JEE 2026 Morning", # replace - with space + title
    "subject": "Physics",           # title case
    "email": "rahul.sharma@gmail.com" # stripped + lowercase
}
"""

def student_detail(student):
    return{
        "name": student["name"].strip().title(),
        "batch":student["batch"].replace("-"," ").title(),
        "subject": student["subject"].title(),
        "email": student["email"].strip().lower()
    }

print(student_detail(student))



#-----------------------------
batch ="IIT-JEE-2026-MORNING"

print(batch.split("-"))
print(batch.startswith("IIT"))
print(batch.endswith("MORNING"))
print("2026" in batch)
print(len(batch))


#---------------

#Write a function called analyze_batch that takes a batch code like "IIT-JEE-2026-MORNING" and returns:
"""
{
    "original": "IIT-JEE-2026-MORNING",
    "parts": ["IIT", "JEE", "2026", "MORNING"],
    "year": "2026",
    "is_morning": True,
    "is_iit": True,
    "total_chars": 20
}

"""


batch="IIT-JEE-2026-MORNING"

def analyze_batch(batch):
    parts = batch.split("-")
    return{
        "orignal": batch,
        "parts" : batch.split("-"),
        "year": parts[2],
        "is_morning": batch.endswith("MORNING"),
        "is_iit": batch.startswith("IIT"),
        "total_chars": len(batch)

    }

print(analyze_batch(batch))