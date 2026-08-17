text ="Hello I am learning Programning"

print(text.lower())
print(text.upper())
print(text.title())



messy = "  hello world  "
print(messy.strip())     # "hello world" (removes whitespace)

price = "$19.99"
print(price.strip("$"))  # "19.99"


# finding and replacing

message = "I love Python programming with Python"

print("Python" in message)

print(message.startswith("I"))

print(message.endswith("Python"))


# find position

print(message.find("Python"))
print(message.count("Python"))

#Replace

new_message = message.replace("Python","JavaScript")

print(new_message)


