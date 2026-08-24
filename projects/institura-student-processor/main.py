
from processor import load_students, analyze_batch, filter_by_batch, generate_report, get_student_summary

def main():
    students = load_students("sample_students.csv")

    while True:
        print("\n===================================\n")
        print("      INSTITURA STUDENT PROCESSOR    ")
        print("\n===================================\n")
        print("1. View overall Analysis")
        print("2. View IIt-JEE Batch Analysis")
        print("3. View NEET Batch Analysis")
        print("4. Generate Report File")
        print("5. Exit")
        print("===================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            choice1 = analyze_batch(students)
            print(choice1)
        elif choice == "2":
            iit = filter_by_batch(students, "IIT-JEE-2026")
            choice2 = analyze_batch(iit)
            print(choice2)

        elif choice == "3":
            neet = filter_by_batch(students, "NEET-2026")
            choice3 = analyze_batch(neet)
            print(choice3)

        elif choice == "4":
            choice4 =generate_report(students,"institura_report.txt")
            print(choice4)
        

        elif choice == "5":
            print("Goodbye!!")
            break

        else:
            print("Invalid choice. Please enter 1-5.")

main()
        


