"""
extend()
remove()
pop()


"""

fruits = ["mango","Orange","Banana",'Grapes']

#extend - it is used when we need to add more than one items the list
# list.extent(["a","b"])
print(fruits.extend(["kiwi","Papaya"]))
fruits.extend(["kiwi","Papaya"])
print(fruits)

#lets see what will happen if we use append insted of extend
fruits = ["mango","Orange","Banana",'Grapes']
fruits.append(["kiwi","Papaya"])
print(fruits)



#remove() - used to remove the items from the list
#Syntax - list.remove("a")

fruits = ["mango","Orange","Banana",'Grapes',"Orange"]
fruits.remove("Orange") # it is only going to remove the first item from the list
print(fruits)

#pop() - it is used to remove the item from the list using index

fruits = ["mango","Orange","Banana",'Grapes',"Orange"]
fruits.pop(2) # if we do not provide any index thenit it wil delete the last one 
print(fruits)