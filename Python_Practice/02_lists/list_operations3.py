"""
reverse()
sort()
count()
membership operation

"""

#reverse() - it is used to reverse the order of items in the list
#syntax -- list.reverse()

numbers = [2,4,1,9,-3,-8]
print(numbers)
numbers.reverse()
print(numbers)


#sort() - it is used to sort the numbers in the list
#syntax - list.sort()

numbers = [2,4,1,9,-3,-8]
numbers.sort()

print("Sorted list:", numbers)


# sort in reerse order

numbers = [2,4,1,9,-3,-8]
numbers.sort(reverse=True)
print(numbers)

#count() - it is used to count how many times the number is being occures in the list

numbers = [0,1,4,2,7,0,9,0,3,0,2,-1]
item_to_count = int(input("which number you want to count from the list:"))
c = numbers.count(item_to_count)
print(f"{item_to_count} in coming in the list {c} times ")


#membership operation

language = ["Python","java","c++"]
print("Python" in language)
print("Python" not in language)
print("JavaScript" in language)

