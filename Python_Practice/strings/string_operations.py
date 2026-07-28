
s1 = "Python is fun"
print(s1[0])
print(s1[-1])
print(len(s1))

language = "Python"
version = "3.13.3"
print(language + version)
print("Python" = "p") # it will give error



s2 = "Python"
print(s2*3)

# In sarings, '*' is repitation operator

# Membership operation
# in

s1 ="Python is fun"
print("Python" in s1)

print("z" in s1)


# not in - this is  reverse of in

print("Python" not in s1)
print("java" not in s1)

# Comparision of string

print("Python"=="Python")
print("Python"=="Python ")

# Removing  spaces from a string - strip()

s1 ="    Python "

print(s1.strip() == "Python")

# replace()


s1 = "We are learning Python"

print(s1)
print(s1.replace("Python","Java"))

print(s1.replace("e","E",count=1)) # count=1 means that it will only replace the one "e"



#counting substrings from strings
#count()
#string.count(substring)

s1 = "we are learning Python. Python is fun"

s2 = "Python"
s3 = "e"

print(f"Occurencess of {s2} in {s1.count("Python")}")
print(f"Occurencess of {s3} in {s1.count("e")}")


#changing case of string
# upper(), lower(), title(), capitalize()


s1 = "We are learning Python. Python is FUN!!"

print(s1.upper())
print(s1.lower())
print(s1.title())
print(s1.capitalize()) # it capitalize only the first letter of the string

# Staring and Ending of String

s1 = "We are learning Python"

#string.startswith(substring)

print(s1.startswith("We"))

# string.endswith(substring)

print(s1.endswith("Python"))
