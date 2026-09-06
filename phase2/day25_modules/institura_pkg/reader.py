def read_students(filepath: str) -> list[dict]:
    students = []
    with open(filepath, "r") as file:
        lines = file.readlines()
    for line in lines[1:]:
        line = line.strip()
        if not line:        # skip empty lines
            continue
        parts = line.split(",")
        if len(parts) < 10:    # skip corrupted lines
            continue
        students.append({
            "roll_number": parts[0],
            "name": parts[1],
            "batch": parts[2],
            "academic_year": parts[3],
            "personal_email": parts[4],
            "phone": parts[5],
            "parent_name": parts[6],
            "parent_phone": parts[7],
            "marks": parts[8],
            "fee_status": parts[9]

        })
    return students