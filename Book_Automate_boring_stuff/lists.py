
#getting sublist with slice
animals = ["cat","bat","rat","elephant"]
print(animals[0:4])  #this means all the values in the list start from 0th positon till 3rd position (4-1)th

animals[:2]
animals[3:] #starts from the (3+1)th postion

#-----------------------

#get a list's length with len()

spam = ["cat","bat","rat","elephant"]

len(spam)

#-----------------


#changing value in list with indexes

spam = ["cat","bat","rat","elephant"]

spam[0] = "lion"

print(spam)

spam[2]=spam[1]
print(spam)

spam[-1] = 23444

print(spam)

#---------------------------

# list concatenation and List 

[1,2,3] + ["A","b","C"]

spam = [1,2,3]
spam = spam + ["A","b","C"]
print(spam)


# Removing values from list with del statement

spam = ["cat","bat","rat","elephant"]

del spam[1:3]

print(spam)



#------------------------------

#-------------Methods----------------#

#finding a value in a list with index() method

spam = ["hello","hi","howdy","heyas"]
spam.index("heyas")

spam.index("hello")

#-----------------------------------------------

#Adding values to lists using append() and insert() method- these methods can only be used in the list value

spam = ["cat","dog","bat"]
spam.append("moose")
print(spam)

spam.insert(1,"chicken")
print(spam)


#removing values from the list with remove()

spam = ["cat","dog","bat"]
spam.remove("cat")
print(spam)