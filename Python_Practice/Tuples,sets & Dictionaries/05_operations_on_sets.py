student1 = {"Physics","Chemistry","Maths","cs"}
student2 = {"Physics","Chemistry","Biology"}
student3 = {"Sanskrit","Maths","cs"}

# common subjests - intesection

common_subject = student1.intersection(student2 )
common_subject = student1 & student2

print(common_subject)
# If their is

# All the subjects student1 and student2 -  Unnion

all_subject = student1.union(student2,student3) 
all_subject = student1 | student2 | student2

print(all_subject)


# Difference of sets

days = {"Mon","Tue","wed","Thrus","fri","Sat","Sun"}
weekends = {"Sat","Sun"}

weekdays = days - weekends # or wee can use the days.difference(weekends)
print(weekdays)



# Frozen sets  - Imutable sets
fs1 = frozenset({10,20,30})
print(fs1, type(fs1))

fs2 = frozenset({10,20,300})

print(fs1 & fs2)
print(fs1 | fs2)