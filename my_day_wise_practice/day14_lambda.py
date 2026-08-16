
# Exercise - 1 Basic lambda
# 1. Takes a number, returns it doubled
double = lambda n : n*2

# 2. Takes a name, returns it in title case
format_name = lambda name : name.title()

# 3. Takes marks, returns "Pass" if >= 40 else "Fail"
classify = lambda n : "Pass" if n >=40 else "Fail"
 
print(double(5))
print(format_name("rahul sharma"))
print(classify(85))
print(classify(30))


# Exercise - 2 Lambda with sorted()

students = [
    {"name": "Rahul Sharma", "batch": "IIT-JEE", "marks": 85},
    {"name": "Priya Patel", "batch": "NEET", "marks": 92},
    {"name": "Amit Kumar", "batch": "IIT-JEE", "marks": 78},
    {"name": "Sneha Singh", "batch": "NEET", "marks": 96},
    {"name": "Rohan Verma", "batch": "IIT-JEE", "marks": 88}
]

sorted_marks = sorted(students,  key=lambda s : s["marks"])
print(sorted_marks)
sorted_marks_reversed = sorted(students,  key=lambda s : s["marks"], reverse = True)
print(sorted_marks_reversed)
sorted_names = sorted(students, key=lambda n:n["name"])
print(sorted_names)


# remember that keys are defined for the dictionaries so that lamda functio will know on which key it has to filter

# Exercise -3 Lambda with filter() and map()

# filter - keep only IIT-JEE students
iit_students = list(filter(lambda s : s["batch"]=="IIT-JEE", students))
print(iit_students)

# map — add grade to every student
# A if marks >= 90, B if >= 75, C otherwise

graded = list(map(lambda s : {**s, "grade": "A" if s["marks"]>= 90 else "B" if s["marks"]>=75 else "C"},students))
print(graded)

#-------------------------------------


# Without lambda — extra function you'll never use again
def get_marks(s):
    return s["marks"]

sorted(students, key=get_marks)

# With lambda — clean, inline, no clutter
sorted(students, key=lambda s: s["marks"])
