from data import Student

def analyze_batch(students: list[Student])-> dict:
    if not students:
        return {}

    marks_list = [s.marks for s in students]  # dot notation  - Pydantic
    topper = max(students, key = lambda s : s.marks)
    pass_count = sum(1 for s in students if s.marks >= 40) # generator expression
    fail_count = len(students) - pass_count
    paid_count = sum(1 for s in students if s.fee_status =="paid")
    pending_count = len(students) - paid_count

    return {
        "total" : len(students),
        "average": round(sum(marks_list) / len(marks_list), 2),
        "topper":topper.name,
        "topper_marks": topper.marks,
        "pass_count": pass_count,
        "fail_count": fail_count,
        "paid_count": paid_count,
        "pending_count": pending_count,
    }

def get_batch_name(students: list[Student])-> list[str]:
    return  list({s.batch for s in students})

def filter_by_batch(students:list[Student], batch:str)-> list[Student]:
    return [s for s in students if s.batch == batch]


if __name__ == "__main__":
    from data import load_students
    students =load_students("sample_students.csv")
    print(analyze_batch(students))
    print(get_batch_name(students))
