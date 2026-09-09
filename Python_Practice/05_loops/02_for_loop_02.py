
s1 = "Hello World"

for char in s1:
    print(char)
print("End of the loop")


employee = {"empid" : 1000,
            "name" : "John",
            "department": "HR"


         }

for i in employee:
    print(i) #this will only print the keys
    print(i, employee[i]) # this will print both


#--------------



employee = {"empid" : 1000,
            "name" : "John",
            "department": "HR"


         }

print(employee.items())

for i in employee.items():
    print(i)

for i in employee.items():
    print(i[0])

for i in employee.items():
    print(i[1])