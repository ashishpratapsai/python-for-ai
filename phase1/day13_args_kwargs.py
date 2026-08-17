# *args

def add(*arg):
    print(arg)
    return sum(arg)

print(add(1,2))
print(add(1,2,4))
print(add(1,2,3,4))

# **kwargs

def show_students(**kwargs):
    print(kwargs)
    print(type(kwargs))

show_students(name = "Rahul", batch = "IIT-JEE" ,marks = 85)
show_students(name = "Priya", batch = "NEET" )

#------------------

def calculate_total(*args):
    total = sum(args)
    average = total / len(args)
    return {
        "total": total,
        "average" : average
    }

print(calculate_total(85, 92, 78))
print(calculate_total(90, 88, 76, 95, 82))





def create_student(**kwargs):
    return(kwargs)

print(create_student(name="Rahul", batch="IIT-JEE", marks=85))
print(create_student(name="Priya", batch="NEET"))

#------------

def create_report(*args,**kwargs):
    marks = (args)
    total = sum(args)
    average = total/len(args)
    details_of_students = (kwargs)

    return {
        "name": details_of_students["name"],
        "batch" : details_of_students["batch"],
        "marks" :marks,
        "total" : total,
        "average" : float(average)
    }

print(create_report(85, 92, 78, name="Rahul", batch="IIT-JEE-2026"))



# we don't need to save the (kwargs) in a details_of_students as a dictionary it is already a dictionary
"""
"name": kwargs["name"],
"batch": kwargs["batch"],
Or even cleaner — since kwargs is already a dictionary, you can use .get() for safety:
"name": kwargs.get("name", "Unknown"),
"batch": kwargs.get("batch", "Unknown"),

"""


#--------------------

def create_report(*args,**kwargs):
    marks = (args)
    total = sum(args)
    average = total/len(args)

    return {
        "name": kwargs.get("name","unknown"),
        "batch" :kwargs.get("batch","unknown"),
        "marks" :marks,
        "total" : total,
        "average" : float(average)
    }

print(create_report(85, 92, 78, batch="IIT-JEE-2026"))