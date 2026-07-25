def greet(name):
   return f"hello {name}"

hi = greet("Ashish")
print(hi)



def calculation(a,b,operation):
   if operation == "add":
      return a+b
   elif operation =="multiply":
      return a*b
   else:
      return "no operation"
   
addition = calculation(2,4,"add")
print(addition)
multi = calculation(2,4,"multiply")
print(multi)

calculations = [(2, 4, "add"), (3, 8, "multiply"), (10, 5, "add")]

for item in calculations:
   print(calculation(item[0],item[1],item[2]))