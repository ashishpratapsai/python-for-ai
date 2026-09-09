from cleaner import clean_student

def test_clean_student_strip_name():
    raw = {
        "roll_number": "R001",
        "name": "  rahul SHARMA  ",
        "batch": "IIT-JEE-2026",
        "academic_year": "2025-2026",
        "personal_email": "rahul@gmail.com",
        "phone": "9876543210",
        "parent_name": "Rajesh Sharma",
        "parent_phone": "9876543211",
        "marks": "85",
        "fee_status": "paid"
    }
    result = clean_student(raw)
    assert result["name"] == "Rahul Sharma"


def test_clean_student_handles_absent_marks():
        raw = {
            "roll_number": "R001",
            "name": "Rahul SHARMA  ",
            "batch": "IIT-JEE-2026",
            "academic_year": "2025-2026",
            "personal_email": "rahul@gmail.com",
            "phone": "9876543210",
            "parent_name": "Rajesh Sharma",
            "parent_phone": "9876543211",
            "marks": "absent", # bad data
            "fee_status": "paid"
        }
        result = clean_student(raw)
        assert result["marks"] == 0


def test_clean_student_handles_string_marks():
    raw = {
        "roll_number": "R001",
        "name": "Rahul SHARMA  ",
        "batch": "IIT-JEE-2026",
        "academic_year": "2025-2026",
        "personal_email": "rahul@gmail.com",
        "phone": "9876543210",
        "parent_name": "Rajesh Sharma",
        "parent_phone": "9876543211",
        "marks": "85",
        "fee_status": "paid"
    }
    result =clean_student(raw)
    assert result["marks"] == 85


def test_clean_student_email_lowercase():
    raw = {
        "roll_number": "R001",
        "name": "Rahul SHARMA  ",
        "batch": "IIT-JEE-2026",
        "academic_year": "2025-2026",
        "personal_email": " RAHUL@gmail.com",
        "phone": "9876543210",
        "parent_name": "Rajesh Sharma",
        "parent_phone": "9876543211",
        "marks": "85",
        "fee_status": "paid"
    }
    result =clean_student(raw)
    assert result["personal_email"] == "rahul@gmail.com"