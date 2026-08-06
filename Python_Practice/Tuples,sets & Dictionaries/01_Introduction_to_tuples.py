#tuple
# they are like lists but are imutable we cannot add or subtract any thing from them 
# sequence of item as the colection
t1 =("Python",45,6.3,True,None,[1,2,3],(3,8,9))


#Accesing item s of tuple
print(t1[-1])

print(t1[-1][-1])

#tuples can be changed to lists and vise versa

fruits = ("mango","orange","Banana")
print(fruits,type(fruits))
fruits = list(fruits)
print(fruits,type(fruits))
