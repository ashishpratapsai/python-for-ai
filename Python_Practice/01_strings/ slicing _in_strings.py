

s1 = "Hello my name is Ashish Pratap Singh"


print(len(s1)) #getting the length of string

print(s1[0]) # getting first letter of string

print(s1[-1]) # Getting last letter of string


"""
Syntax of indexing: string[index]
Syntax of slicing: string[start:end:step]
- start: starting index at which the slicing operation starts
- end: ending index at which the slicing stops (excluded)
- step: integer that specifies the step for the slicing

"""

s1_slice = s1[2:7:1]


print(s1_slice)

print(s1[2:7:2])