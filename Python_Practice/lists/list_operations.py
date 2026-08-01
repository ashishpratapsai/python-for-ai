
s1 =[2,7,0,9,5,6]

#slicing the string

print(s1[1:4:1])

s2=[1,2,3,4,5,6]

#concatination of list
print(s1+s2)


# repetation of lists

print(s1*3) # it will repeat the list 3 times 


# adding some thing in the list 
# list.append() -- Syntax - this is basically going to add the item in the end

fruits = ["banana","Orange","mango"]

print(fruits.append("papaya")) # it will append but it will not rint , means thee list is being updated but will not print 


fruits.append("grapes")
print(fruits)


# if we have to insert the item in the list
# syntax - list.insert(index,item)


fruits.insert(1,"tomato")

print(fruits)






