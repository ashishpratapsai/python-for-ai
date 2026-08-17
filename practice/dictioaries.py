


person ={
    "name" : "Ashish",
    "age" : 29,
    "city" : "mumbai"
}

print(person["name"]) 
print(person["age"]) 

print(person.get("job"))
print(person.get("job","unknown"))

person["email"] = "ashish@gmail.com"

print(person)

print(person.keys())

print(person.values())

print(person.items())

if "mam" in person:
    print("Name Found!")
else:
    print("Not found")

person.update({"age":31,"job":"Ai Automation"})

# Dictionary of dictionaries
students = {
    "alice": {"age": 20, "grade": "A"},
    "bob": {"age": 21, "grade": "B"},
    "charlie": {"age": 19, "grade": "A"}
}

# Access nested data
print(students["alice"]["grade"])  # "A"