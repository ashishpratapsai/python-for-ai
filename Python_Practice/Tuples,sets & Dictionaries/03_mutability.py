# Mutability & Immutability
# Lists are mutable
# Tuples and Strings are imutable

s1 = "Python is fun"
s2 = s1.replace("Python","Java")
print(s1) # we can see that s1 is not changed
print(s2) # So when we stored in another variable it changed 

l1 = ("Mango","Banana","Apple")
l1.append("Grapes")
print(l1)   #their is no append function for tuples

l1 = ["Mango","Banana","Apple"]
l1.append("Grapes")
print(l1) # we can see that we can add items to lists