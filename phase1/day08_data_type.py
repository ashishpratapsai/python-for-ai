name = "Ashish"        # str — text, always in quotes
age = 29               # int — whole number
height = 5.9           # float — decimal number
is_active = True       # bool — True or False only
nothing = None         # NoneType — absence of value
videos = [1, 2, 3]    # list — collection of items


print(type("Ashish"))   # <class 'str'>
print(type(29))         # <class 'int'>
print(type(5.9))        # <class 'float'>
print(type(True))       # <class 'bool'>
print(type(None))       # <class 'NoneType'>


print("29" + "1")   # "291" — string joins
print(29 + 1)       # 30 — number adds


int("29")      # "29" → 29
str(29)        # 29 → "29"
float("5.9")   # "5.9" → 5.9
bool(0)        # 0 → False
bool(1)        # 1 → True

# writting the function to describing the value

def describe_value(value):
    return{
        "type": type(value).__name__,
        "value": value
    }

print(describe_value("Ashish"))
print(describe_value(29))
print(describe_value(5.9))
print(describe_value(True))
print(describe_value(None))


#------------------

def describe_value(value):
    return{
        "type": type(value).__name__,
        "value": value,
        "can_do_maths": type(value).__name__ == "int" or type(value).__name__ == "float" 

    }

print(describe_value("Ashish"))
print(describe_value(29))
print(describe_value(5.9))
print(describe_value(True))
print(describe_value(None))


#----------------

def safe_to_number(value):
    try:
        number=int(value)
        return number
    except:
        return None

print(safe_to_number("Ashish"))
print(safe_to_number("30"))

result = safe_to_number("30")
print(result)
print(type(result))