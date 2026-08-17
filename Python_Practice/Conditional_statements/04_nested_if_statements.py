"""
if marks>= 60, student is pass else student is fail
and the student is pass, then we print the gradde

    >=90, grade A
    b/w 80 and 89 grade B
    b/w 70 and 79 grade c
    b/w 60 and 69 grade D

"""

marks = float(input("Enter your marks to know your grade: "))

if marks >=60:
    print("Congrats! you have passed the exam")

    if marks >=90:
        print("Your grade is: A")
    elif 80<= marks <90:
        print("Your grade is: B")
    elif marks>=70 and marks <80:
        print("Your grade is: C")
    elif marks>=60 and marks<70:
        print("Your grade is: D")
    else:
        print("Your grade is: F")
else:
    print("Sorry you Failed your exam, Study hard next time") 