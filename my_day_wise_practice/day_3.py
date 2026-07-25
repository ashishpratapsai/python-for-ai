
numbers = [1,2,3,4,5]

for number in numbers:
    print(number)

#------------

words = ["n8n","python","automation"]

for word in words:
    print("I am learning"+" " + word)


#------------------



def calculate(a,b,operation):
    if operation == "add":
        return a+b
    elif operation == "multiply":
        return a*b
    else:
        return "No Operation"


calculations = [(2,4,"add"),(3,4,"multiply"),(10,5,"sub")]
    
for item in calculations: 
    print(calculate(item[0],item[1],item[2]))

#---------

"""

calculation = [
    (2,   4,   "add"),       ← item on loop 1
     ↑    ↑      ↑
   [0]  [1]    [2]

    (3,   4,   "multiply"),  ← item on loop 2
    (4,   4,   "sub")        ← item on loop 3
]
"""


videos = [
    "How to use Claude Code",
    "n8n tutorial for beginners",
    "Python for AI automation",
    "Building agents with LangChain"
]

for index, video in enumerate(videos,1):
  print( f"{index}.{video}")



  