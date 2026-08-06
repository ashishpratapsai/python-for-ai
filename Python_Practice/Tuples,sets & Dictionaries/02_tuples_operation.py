"""
concatenation, repetation, membership
count, index
min,max,sum

"""

#Concatenation 

t1 = ("Python", 10)
t2 = (20,4,-4,9)

print(t1+t2)

#repetation
print(t1*3)

#membership

print(10 in t1)
print(5 not in t1)
print("Python" not in t1)

# Count

t1 = ( 1,3,7,1,9,0,5,3)
print(t1.count(1))
print(t1.count(100))

# Index
# tuple.index(element)
t1 = ( 1,3,7,1,9,0,5,3)
print(t1.index(1)) # it only tells the index when it is first found

# min, max ,sum
print(f"Smallest number {min(t1)}")
print(f"Biggest number {max(t1)}")
print(f"Sum of  numbers {sum(t1)}")
