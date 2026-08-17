#if-else

# if condition:
#     # block of code is executed when the condition is true
# else:
#     # block of code is executed when the condition become false



age = float(input("what is your age?: "))

if age >= 18:
    print("Congratulations you are an adult. you can now vote!!!!")
else:
    print("A few more years before you can vote.")
print("Rest of the prgram")


# Print if a (int) is odd or even 
#even - when the number is fully divisible by 2 remainder is 0
#odd - the number is not divisible by 2. remainder is not 0
# %

number = int(input("Enter a number to check if it is even or odd : "))

if number%2 ==0:
    print("It is an even number")
else:
    print("It is an odd number")


#check whether the number is positive or negative

num = int(input("enter a number:"))

if num <0:
    print("it is negative ")
else:
    print("it is positive")