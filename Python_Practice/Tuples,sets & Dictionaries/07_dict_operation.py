student1 ={"maths":80.5,"eng":70.6 ,"phy":89.0}

print(student1["maths"]) # using this we fetch the value of the key

#but what is that key is not present in the dict then we use .get()

print(student1.get("chem")) # it will give us none as chem is not present- useto avoid the error

print(student1.get("Chem", 90))

# another example

emp1 ={"id" : 1001, "name": "Jhon", "salary":10000}

print(emp1.get("phone", 8723937832)) # whem providig the value if the key is not present the it willl return that value

# if the value is they in the dict then it will only send the default alue , this is how we can handle the error

print(emp1.get("id", 9797979))

# membership operator - in

print(1001 in emp1) # it does not look for the value it look for the key
print("name" in emp1)

# how to update or create the key vlue in dict

emp1["phone"] =89823479493
print(emp1)


#------------------

sem1_marks = {
    "maths":78.5,
    "phy":87,
    "chem": 90


}

sem2_marks = {
    "eng":77,
    "comp":70.8
}

sem1_marks.update(sem2_marks)
print(sem1_marks)


#-------------
groceries_1 = {'milk': 60, "rice": 100 , "biscuits": 20}
groceries_2 = {'rice': 110, 'bread': 30}
groceries_1.update(groceries_2)
print(groceries_1)

# pop()

groceries_1.pop("milk")
print(groceries_1)

# keys can not be duplicated

groceries_1 = {'milk': 60, "rice": 100 , "biscuits": 20,"milk":70}
print(groceries_1)



#not allowed keys - list, set, dict => mutable datatypes
#allowed keys - str, int, float, bool, tuple = immutable datatypes
#keys of a dictionary can only be mutable datatype

# Values can be any datatype
student1 = {
    "id" : 10001,
    "name" : "John",
    "marks" : {
        "eng" : 78,
        "maths": 89
    }
}

print(student1["marks"]["eng"])

#fetch the keys

#keys()
print(student1.keys())

#values()
print(student1.values())

#items()
print(student1.items()) # will give you in formo of tuples