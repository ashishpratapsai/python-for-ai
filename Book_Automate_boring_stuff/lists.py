
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


