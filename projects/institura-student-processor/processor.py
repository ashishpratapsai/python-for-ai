def read_students(filepath):
    students = []
    with open(filepath, "r") as file:
        lines =file.readlines()
    for line in lines[1:]: # will skip the first line
        line = line.strip()
        parts =line.split(",")
        students.append({
             "roll_number": parts[0],
            "name":parts[1] ,
            "batch": parts[2],
            "academic_year": parts[3],
            "personal_email": parts[4],
            "phone": parts[5],
            "parent_name": parts[6],
            "parent_phone": parts[7],
            "marks": parts[8],
            "fee_status": parts[9]
        })
    return students

def clean_student(student):
    try:
        marks = int(student["marks"])
    except ValueError:
        marks = 0

    return { 
         "roll_number": student["roll_number"].strip(),
        "name": student["name"].strip().title(),
        "batch": student["batch"].strip(),
        "academic_year": student["academic_year"].strip(),
        "personal_email": student["personal_email"].strip().lower(),
        "phone": student["phone"].strip(),
        "parent_name": student["parent_name"].strip().title(),
        "parent_phone": student["parent_phone"].strip(),
        "marks": marks,
        "fee_status": student["fee_status"].strip().lower()

    }  
#now combining both the function  

def load_students(filepath):
    raw_students = read_students(filepath)
    return [clean_student(student) for student in raw_students]

# students =load_students("sample_students.csv")
# for student in students:
#     print(student)



# students =read_students("sample_students.csv")
# for student in students:
#      print(student)
# this is after writhing the one function 


# students =read_students("sample_students.csv")
# for student in students:
#     cleaned = clean_student(student)
#     print(cleaned)
# this writing the two funcyions without combining

def get_student_summary(student):
    marks = student["marks"]
    grade = "A" if marks >=90 else "B" if marks >= 75 else "C" if marks >= 40 else "F"
    status = "Pass" if marks >=40 else "Fail" 
    return {
        "roll_number" : student["roll_number"],
        "name" : student["name"],
        "marks": marks,
        "grade" : grade,
        "status" : status,
        "fee_status" :student["fee_status"]

    }


students =load_students("sample_students.csv")
for student in students:
    print(get_student_summary(student))
