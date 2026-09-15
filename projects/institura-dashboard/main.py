from data import load_students
from analyzer import analyze_batch, get_batch_name, filter_by_batch
from reporter import generate_report
import logging

logging.basicConfig(
    level = logging.INFO,
    format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

def main():
    print("\n=== INSTITURA ANALYTICS DASHBOARD ===\n")

    students = load_students("sample_students.csv")

    if not students:
        print("No student found.")
        return

    overall = analyze_batch(students)
    print(f"Total Student : {overall["total"]}")
    print(f"Average Marks : {overall["average"]}")
    print(f"Topper : {overall["topper"]} ({overall["topper_marks"]} marks)")
    print(f"Pass: {overall["pass_count"]} | Fail: {overall["fail_count"]}")
    print(f"Fee Paid: {overall["paid_count"]} | Pending: {overall["pending_count"]}")

    generate_report(students)
    print("\nDashboard complete")

if __name__ == "__main__":
    main()    