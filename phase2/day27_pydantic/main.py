from models import Student
from models import StudentV2

# vadid syntax - this should work
student1 = Student(
    roll_number ="R001",
    name = "Rahul Sharma",
    batch = "IIT-JEE-2026",
    academic_year = "2025-2026",
    personal_email = "rahul@gmal.com",
    phone="9876543210",
    parent_name = "Rajesh Sharma",
    parent_phone = "9876543211",
    marks = 85,
    fee_status="paid"
)
# print(student1)
# print(student1.name)
# print(student1.marks)

# This should fail — marks is a string not int
student2 = Student(
    roll_number="R002",
    name="Priya Patel",
    batch="NEET-2026",
    academic_year="2025-2026",
    personal_email="priya@gmail.com",
    phone="9876543212",
    parent_name="Suresh Patel",
    parent_phone="9876543213",
    marks="85",
    fee_status="paid"
)


# print(student2)
# print(student2.name)
# print(student2.marks)

# Test 1 — negative marks
student = StudentV2(
    roll_number="R001",
    name="  rahul SHARMA  ",
    batch="IIT-JEE-2026",
    academic_year="2025-2026",
    personal_email="rahul@gmail.com",
    phone="9876543210",
    parent_name="Rajesh Sharma",
    parent_phone="9876543211",
    marks=-50,
    fee_status="paid"
)
print(student.name)