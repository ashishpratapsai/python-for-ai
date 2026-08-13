print(int("absent"))

#----------

try:
    marks = int("absent")
except ValueError:
    mark = 0
    print("Invalid marks - setting to 0")

print(mark)


#-------------
"""
Write a function called safe_parse_student that takes a raw student 
record and returns a clean one — without crashing on bad data.
# This is messy real-world data — some fields are wrong
student = {
    "name": "  rahul sharma  ",
    "marks": "absent",
    "age": "seventeen",
    "email": "Rahul.sharma@gmail.com"
}

ANS

{
    "name": "Rahul Sharma",
    "marks": 0,          # default when marks can't be parsed
    "age": None,         # default when age can't be parsed
    "email": "rahul.sharma@gmail.com"
}
"""
# This is messy real-world data — some fields are wrong
student = {
    "name": "  rahul sharma  ",
    "marks": "absent",
    "age": "Seventeen",
    "email": "Rahul.sharma@gmail.com"
}

def safe_parse_student(student):
    try:
        marks = int(student["marks"])
        age = int(student["age"])  # wrong 
    except ValueError:
        marks =0
        age = None

    

    return{
        "name": student["name"].strip().title(),
        "marks" : marks,
        "age" : age,
        "email": student["email"].strip().lower()
    }


print(safe_parse_student(student))
"""
#the mistake i am making here is both the conversation are in same try block So if marks fails — Python jumps to except immediately and never tries age
Both get default values even if only one failed.

"""

# correct 
student = {
    "name": "  rahul sharma  ",
    "marks": "absent",
    "age": "17",
    "email": "Rahul.sharma@gmail.com"
}

def safe_parse_student(student):
    try:
        marks = int(student["marks"])
    except ValueError:
        marks =0
    try:
        age = int(student["age"]) # this is correct 
    except ValueError:    
        age = None

    

    return{
        "name": student["name"].strip().title(),
        "marks" : marks,
        "age" : age,
        "email": student["email"].strip().lower()
    }


print(safe_parse_student(student))



#key error

student = {
    "name": "rahul sharma",
    "marks": "85"
}



try:
    email = student["email"]
except KeyError:
    email = "no-email@unknown.com"

print(email)

# another way using .get() function
student = {
    "name": "rahul sharma",
    "marks": "85"
}
print(student.get("email","no-email@unknown.com"))
print(student.get("name","unknown"))

#----------------
student = {
    "name": "  rahul sharma  ",
    "marks": "absent"
    # age and email completely missing
}

def safe_parse_student(student):
    try:
        marks = int(student["marks"])
    except ValueError:
        marks = 0
    return {
        "name" : student.get("name","Unknown").strip().title(),
        "marks" : marks,
        "age" : student.get("age",None),
        "email" : student.get("email","no-email@unknown.com")

    }

print(safe_parse_student(student))

# learning - alays use .get( function while dealing with dictionary to avoid error)


#type error

student_name = None

print(student_name.strip())