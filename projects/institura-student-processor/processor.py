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

# students =load_students("sample_students.csv")
# for student in students:
#     print(get_student_summary(student))


def analyze_batch(students):
    marks_list = [s["marks"] for s in students]
    # topper — use max with lambda like day 14 
    topper = max(students , key = lambda s : s["marks"])
    #counts -loop and count
    pass_count = 0
    fail_count = 0
    paid_count = 0
    pending_count =0 



    for student in students:
        if student["marks"] >=40:
            pass_count += 1
        else:
            fail_count += 1
        if student["fee_status"] == "paid":
            paid_count += 1
        else:
            pending_count += 1

    
    return{
        "total_student" : len(students),
        "topper": topper["name"],
        "topper_marks" : max(marks_list),
        "average_marks": sum(marks_list)/ len(marks_list),
        "highest_marks": max(marks_list),
        "lowest_marks": min(marks_list),
        "pass_count": pass_count,
        "fail_count": fail_count,
        "paid_count": paid_count,
        "pending_count": pending_count

        
    }



# students =load_students("sample_students.csv")

# print(analyze_batch(students))



def filter_by_batch(students, batch_name):
    return [s for s in students if s["batch"] == batch_name]
students =load_students("sample_students.csv")
iit = filter_by_batch(students, "IIT-JEE-2026")
neet = filter_by_batch(students, "NEET-2026")

print("IIT-JEE Analysis:")
print(analyze_batch(iit))

print("NEET Analysis:")
print(analyze_batch(neet))


def generate_report(students,filename):
    overall = analyze_batch(students)
    iit = filter_by_batch(students, "IIT-JEE-2026")
    iit_analysis = analyze_batch(iit)
    neet = filter_by_batch(students, "NEET-2026")
    neet_analysis = analyze_batch(neet)


    with open(filename, "w") as file:
        file.write("========================================\n")
        file.write("      INSTITURA STUDENT REPORT\n")
        file.write("========================================\n")
        file.write("\nOVERALL ANALYSIS\n")
        file.write("-----------------\n")
        file.write(f"Total Students : {overall["total_student"]}\n")
        file.write(f"Topper         : {overall["topper"]} ({overall["topper_marks"]})\n")
        file.write(f"Average Marks  : {overall["average_marks"]:.2f} \n")
        file.write(f"Lowest Marks   : {overall["lowest_marks"]} \n")
        file.write(f"Pass Count     : {overall["pass_count"]} \n")
        file.write(f"Fail Count     : {overall["fail_count"]} \n")
        file.write(f"Paid Fees      : {overall["paid_count"]} \n")
        file.write(f"Pending Fees   : {overall["pending_count"]} \n")

         #IIT section

    
        file.write("\nIIT-JEE-2026\n")
        file.write("-----------------\n")
        file.write(f"Total students : {iit_analysis["total_student"]}\n")
        file.write(f"Topper         : {iit_analysis["topper"]} ({iit_analysis["topper_marks"]})\n")
        file.write(f"Average Marks  : {iit_analysis["average_marks"]:.2f}\n")
        file.write(f"Lowest Marks   : {iit_analysis["lowest_marks"]}\n")
        file.write(f"Pass Count     : {iit_analysis["pass_count"]}\n")
        file.write(f"Fail Count     : {iit_analysis["fail_count"]}\n")
        file.write(f"Paid Count     : {iit_analysis["paid_count"]}\n")
        file.write(f"Pending Fees   : {iit_analysis["pending_count"]}\n")


        # NEET sectiion


        file.write("\nNEET-2026\n")
        file.write("------------\n")
        file.write(f"Total Student : {neet_analysis["total_student"]}\n")
        file.write(f"Topper        : {neet_analysis["topper"]} ({neet_analysis["topper_marks"]})\n")
        file.write(f"Average Marks : {neet_analysis["average_marks"]:.2f}\n")
        file.write(f"Lowest Marks  : {neet_analysis["lowest_marks"]}\n")
        file.write(f"Pass Count    : {neet_analysis["pass_count"]}\n")
        file.write(f"Fail Count    : {neet_analysis["fail_count"]}\n")
        file.write(f"Paid Count    : {neet_analysis["paid_count"]}\n")
        file.write(f"Pending Count : {neet_analysis["pending_count"]}\n")



        file.write("\nSTUDENT DETAILS\n")
        file.write("------------------\n")
        for student in students:
            summary = get_student_summary(student)
            file.write(f"{summary["roll_number"]} | {summary["name"]} | {summary["marks"]} | {summary["grade"]} | {summary["status"]} | {summary["fee_status"]}\n")
            
        file.write("\n========================================\n")
        file.write("           END OF REPORT\n")
        file.write("========================================\n")

    print(f"Report saved to {filename}")




students =load_students("sample_students.csv")
generate_report(students,"institura_report.txt")