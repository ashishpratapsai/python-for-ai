fruits = ["apple", "banana", "orange"]

# Get items
print(fruits[0])    # "apple" (first item)
print(fruits[1])    # "banana"
print(fruits[-1])   # "orange" (last item)
print(fruits[-2])   # "banana" (second to last)

# Slicing
print(fruits[0:2])  # ["apple", "banana"]
print(fruits[1:])   # ["banana", "orange"]



#-------------


fruits[0] = "mango"
print(fruits)

fruits.append("grapes")
fruits.insert(0,"kiwi")

fruits.remove("banana")
print(fruits)

last = fruits.pop()
print(fruits)

del fruits[1]
print(fruits)


#---------


numbers = [3, 1, 4, 1, 5, 9]

# Information
print(len(numbers))         # 6 (length)
print(numbers.count(1))     # 2 (count occurrences)
print(numbers.index(4))     # 2 (find position)

# Sorting
numbers.sort()              # Sort in place
print(numbers)              # [1, 1, 3, 4, 5, 9]

numbers.reverse()           # Reverse order
print(numbers)              # [9, 5, 4, 3, 1, 1]

# Copy
new_list = numbers.copy()   # Create a copy



#-------------------

fruits = ["mango"]

if "apple" in fruits:
    print("found apple!")
if fruits:
    print("list has items")
else:
    print("list is empty")

