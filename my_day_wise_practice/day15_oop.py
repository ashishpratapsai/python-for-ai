
class Student:
    def __init__(self,name,batch,marks):
        self.name = name
        self.batch = batch
        self.marks = marks

    def get_grades(self):
        if self.marks >= 90:
            return "A"
        if self.marks >= 75:
            return "B"
        else:
            return "C"

    def is_pass(self):
        return self.marks >= 40

    def summary(self):
        return f"{self.name} | {self.batch} | {self.marks} | Grade : {self.get_grades()}"



student1 = Student("Rahul Sharma","IIT-JEE", 85) 
student2 = Student("Priya Patel","NEET", 92) 
student3 = Student("Amit Kumar","IIT-JEE", 35) 

print(student1.summary())
print(student2.summary())
print(student3.summary())
print(student3.is_pass())

#--------------------


class Student:
    def __init__(self,name,batch,marks):
        self.name = name
        self.batch = batch
        self.marks = marks

    def get_grades(self):
        if self.marks >= 90:
            return "A"
        if self.marks >= 75:
            return "B"
        else:
            return "C"

    def get_status(self):
        if self.marks >=90:
            return "Topper"
        if self.marks >=75:
            return "Good"
        if self.marks >=40:
            return "Average"
        if self.marks <40:
            return "Failed"

    def to_dict(self):
        return {
            "name" : self.name,
            "batch" : self.batch,
            "marks" : self.marks,
            "grade" : self.get_grades(),
            "status" : self.get_status(),
            "summary" : self.summary()
        }

    def is_pass(self):
        return self.marks >= 40

    def summary(self):
        return f"{self.name} | {self.batch} | {self.marks} | Grade : {self.get_grades()}"



student1 = Student("Rahul Sharma","IIT-JEE", 85) 
student2 = Student("Priya Patel","NEET", 92) 
student3 = Student("Amit Kumar","IIT-JEE", 35) 

print(student1.to_dict())
print(student2.summary())
print(student3.summary())
print(student3.is_pass())

#-------------------
class Batch:
    def __init__(self, batch_name):
        self.batch_name = batch_name
        self.students = []

    def add_student(self,student):
        self.students.append(student)

    def get_topper(self):
        return max(self.students, key=lambda s : s.marks)

    def get_average(self):
        total =sum(s.marks for s in self.students)
        return total/ len(self.students)

    def get_summary(self):
        return{
            "batch": self.batch_name,
            "total_sudents" : len(self.students),
            "average_marks": self.get_average(),
            "topper" : self.get_topper().name
        }

iit_batch = Batch("IIT-JEE-2026")
iit_batch.add_student(Student("Rahul Sharma", "IIT-JEE", 85))
iit_batch.add_student(Student("Amit Kumar", "IIT-JEE", 78))
iit_batch.add_student(Student("Rohan Verma", "IIT-JEE", 92))

print(iit_batch.get_summary())