

def check_number(n):
    if n>0:
        return "Positive"
    elif n<0:
        return "Negative"
    else:
        return "Zero"
    
print(check_number(5))
print(check_number(-2))
print(check_number(0))

#----------------


def calculate(a,b,operation):
    if operation == "add":
        return a+b
    elif operation == "multiply":
        return a*b
    else:
        return "No Operation"

addition = calculate(2,4,"add") 
print(addition)
multiply = calculate(3,8,"multiply")
print(multiply)

