# Introducrtion and basic operations on sets 


#sets are non-sequential collection of items
#comma seperatedd elements enclosed within{}

# sets do not allow duplicate elements

s1 = { 10,4,10,7,3,7}

print(s1, type(s1))

# we cannot do indexing and slicing of sets 

nums = {10,2,5,7}


# membership operator - in, not in

print(2 in nums)
print(0 not in nums)


# Concatinations? - it cannot be done 

numbs_1 = {1,2,3}
numbs_2 ={5,3,3}

print(numbs_1 + numbs_2)

# repetation ? -  it cannot be done

print(numbs_2 * 3)


#--------------

weekdays = ("Mon","tues","wed","thrus")

weekdays = set(weekdays)
print(weekdays)

# the order is changed as sets do not have any defined order

# Are sets mutable or imutable?

set_1 = {2,0,-1}
print(set_1)
#add()- add elemnts to the sets

set_1.add(5)
print(set_1)

#remove()

set_1.remove(0)
print(set_1)


# what will happen whenif we add the element which is already present?

#discard()

set_1.discard(10)

print(set_1)


# if you want to avoid the errors while using sets then use discard in place of remove