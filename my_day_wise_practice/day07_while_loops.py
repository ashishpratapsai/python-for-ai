

count = 0

while count <5:3
    print(count)
    count = count +1


#----------------------

def ask_until_valid():
    while True:
        number = int(input("Enter a Number between 1 and 10:"))
        if number >=1 and number <= 10:
            return "valid Number"
        else:
            print("Invalid, try Again")


result =ask_until_valid()
print(result)


# now instead of returnin the valid number return the number 


def ask_until_valid():
    while True:
        number = int(input("Enter a Number between 1 and 10:"))
        if number >=1 and number <= 10:
            return number
        else:
            print("Invalid, try Again")


result =ask_until_valid()
print(result)




#Example-2 password checker 

while True:
    password = input("Enter your password:")
    if password == "python123":
         print("Access Granted")
         break



# Example3-

def get_valid_operation():
    while True:
        operation = input("Enter operation(add/muliply/substract):")
        if operation =="add" or operation =="substract" or operation =="multiply":
            return operation
        else:
            print("Invalid operation. try again")

result = get_valid_operation()
print(result)