import time

# the decorator
def timer(func):
    def wrapper(*args, **kwargs):
        start =time.time()
        result = func(*args, **kwargs) # run the orignal output
        end = time.time()
        print(f"{func.__name__} tool {end - start:.2f}s")
        return result
    return wrapper

# using decorators
@timer
def load_student():
    time.sleep(1) # stimulate work
    return ["Rahul","Priya","Amit"]

@timer
def generate_report():
    time.sleep(0.5)
    return "Report generated"


students = load_student()
report = generate_report()
print(students)
print(report)



#------------

# decorator with argument - retry on faliure

def retry(times:int):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(times):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Attempt {attempt +1} failed : {e}")
                    if attempt == times - 1:
                        raise
        return wrapper
    return decorator

# usage

@retry(times=3)
def call_api():
    import random
    if random.random()<0.7: # 70% chance of faliure
        raise Exception("API timeout")
    return "success!"

result = call_api()
print(result)

# layer 3 

import logging
logging.basicConfig(
    level=logging.INFO,
    format = "%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

def log_function(func):
    def wrapper(*args, **kwargs):
        logger.info(f"Calling {func.__name__} with args ={args}")
        result = func(*args, **kwargs)
        logger.info(f"{func.__name__} returned {result}")
        return result
    return wrapper

@log_function
def analyse_batch(batch_name:str) -> dict:
    return {"batch": batch_name, "students": 4, "average": 85}

result= analyse_batch("IIT-JEE-2026")
print(result)