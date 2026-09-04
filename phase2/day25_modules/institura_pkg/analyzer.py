

def analyse_batch(students):
    marks_list = [s["marks"] for s in students]
    topper = max(students, key=lambda s : s["marks"] )
    #counts - loop and count
    pass_count =0
    fail_count = 0
    paid_count = 0
    pending_count = 0

    for student in students:
        if student["marks"]>=40:
            pass_count +=1
        else:
            fail_count += 1
        if student["fee_status"] == "paid":
            paid_count += 1
        else:
            pending_count += 1

    return{
        "total_students": len(students),
        "topper": topper["name"],
        "topper_marks": max(marks_list),
        "average_marks": sum(marks_list)/len(marks_list),
        "highest_marks" : max(marks_list),
        "lowest_marks": min(marks_list),
        "pass_count" : pass_count,
        "fail_count": fail_count,
        "paid_count" : paid_count,
        "pending_count": pending_count
    }


def filter_by_batch(students, batch_name):
    return [s for s in students if s["batch"] == batch_name]