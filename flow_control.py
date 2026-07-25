

temprature = 31

if temprature > 30:
    print("It is very hot")
elif temprature > 25:
    print("It is  hot")
else:
    print("It is normal")

# So basically, at the top we must always put the higher value. As we know, when going from the top to bottom in Python, it executes the first statement of the `else if` thing. Whenever we are putting it at the higher, it will check for that also. Suppose let's take an example: if we put 25 above and 30 below, it will execute the first statement of it because it is the correct, so when you want to make the multiple steps, you start from the higher one. 


age = 32
has_licence = True

if age>=18 and has_licence:
    print("yeah! you can drive the car")
else:
    print("sorry please fulfil the condition")


#------------------------------------

score = 40

if score>=90:
    print("A - Excellent")
elif score >=80:
    print("B - Good Job")
elif score >= 70:
    print("C - keep it Up")
else:
    print("F - Need improvement")    

#----------------------

has_ticket = True
age = 16

if has_ticket:
    if age >=18:
        print("you can enjoy you movie")
    else:
        print("Need adult Supervision")
else:
    print("Buy Ticket")
        
    
