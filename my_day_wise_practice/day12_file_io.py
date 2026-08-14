
# write a file 

with open("student.txt","w") as file:
    file.write("Rahul Sharma, IIT-JEE-2026, 85\n")
    file.write("Prita Patel, NEET-2026, 85\n")
    file.write("Ankit Kumar, IIT-JEE-2026, 85\n")

#reading back the file 

with open("student.txt","r") as file:
    content = file.read()
print(content)

#--------------

"""
Write a function called save_students that
takes a list of student dictionaries 
and saves them to a file called "institura_students.txt".
"""

students = [
    {"name": "Rahul Sharma", "batch": "IIT-JEE-2026", "marks": 85},
    {"name": "Priya Patel", "batch": "NEET-2026", "marks": 92},
    {"name": "Amit Kumar", "batch": "IIT-JEE-2026", "marks": 78}
]

def save_student(students):
        with open("institura_students.txt","w") as file:
         for student in students:
            file.write(f"{student["name"]} | {student["batch"]} | {student["marks"]}\n")

print(save_student(students))



with open("institura_students.txt","r") as file:
    content  = file.readlines()
def read_students(content):
    students= []
    for line in content:
     parts = line.strip().split(" | ")
     students.append({
         "name" : parts[0],
         "batch" : parts[1],
         "marks" : int(parts[2])
     })

     

    return students

print(read_students(content))

print(content)