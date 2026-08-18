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



students =read_students("sample_students.csv")
for student in students:
    print(student)