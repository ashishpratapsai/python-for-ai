"""
>=90, grade A
b/w 80 and 89 grade B
b/w 70 and 79 grade c
b/w 60 and 69 grade D
<60, grade F
"""

# if-elif-else

marks = float(input("Enter your marks to know your grade: "))

if marks >=90:
    print("A")
elif 80<= marks <90:
    print("B")
elif marks>=70 and marks <80:
    print("C")
elif marks>=60 and marks<70:
    print("D")
else:
    print("F")


# if one of the condition is true then rest of the condition will not be checked