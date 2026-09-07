from dotenv import load_dotenv
import os

load_dotenv()

institute_name = os.getenv("INSTITUTE_NAME")
api_key = os.getenv("API_KEY")
debug = os.getenv("DEBUG", "False")
max_student = int(os.getenv("MAX_STUDENTS","100"))

print(f"Institute : {institute_name}")
print(f"API Key : {api_key}")
print(f"Debug : {debug}")
print(f"Max Students : {max_student}")
