from .reader import read_students
#updated: Day 29
import logging

logger = logging.getLogger(__name__)

def clean_student(student:list[dict]) ->dict:
    try:
        marks = int(student["marks"])
    except ValueError:
        logger.warning(f"Invalid marks for {student["roll_number"]}: '{student["marks"]}' - defaulting to 0")
        marks = 0

    return{
        "roll_number": student["roll_number"].strip(),
        "name": student["name"].strip().title(),
        "batch": student["batch"].strip(),
        "academic_year": student["academic_year"].strip(),
        "personal_email": student["personal_email"].strip().lower(),
        "phone": student["phone"].strip(),
        "parent_name": student["parent_name"].strip().title(),
        "parent_phone": student["parent_phone"].strip(),
        "marks": marks,
        "fee_status": student["fee_status"].strip().lower()
    }

def load_students(filepath: str) -> list[dict]:
    raw_students = read_students(filepath)
    return[clean_student(student) for student in raw_students]
