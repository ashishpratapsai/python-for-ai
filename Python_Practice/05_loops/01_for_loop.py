"""
It is an iteator based loop which steps through the items of collection
(lists,tples,sts,dic,str), and execute a block of code repeatedly
 for a number of times equal to the item/elements of that collection

"""

# for var in sequence:
#     statement1
#     statement2
#     .
#     .
#     .
#     statementN

percents = [85.5,76,98,88,55]
# print(percents[0])
# print(percents[1])
# print(percents[2])
# print(percents[3])
# print(percents[4])
# this is not the good way to write the program what if the list is too long

for p in percents:
    print(p)