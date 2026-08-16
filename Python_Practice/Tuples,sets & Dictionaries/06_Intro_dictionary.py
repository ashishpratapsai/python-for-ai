# comma seperated key-values pairs enclosed within {}
# {key1:value1, key2:value2}


groceries = {"milk":60 ,"biscuits":20,"rice":90,"bread":30}
print(groceries)
print(type(groceries))
print(len(groceries))

print(groceries[0]) # key error these do not have indexies

# value can be fethed using key

print(groceries["milk"])

#--------
#dictionaries are mutable


groceries["milk"] = 65
print(groceries)


groceries["eggs"] = 50 # add new key-value pair
print(groceries)