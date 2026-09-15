from datetime import datetime
from data import Student
from analyzer import analyze_batch, get_batch_name, filter_by_batch


def generate_report(students : list[Student], filename:str ="institura_report.md") -> None:
    today = datetime.now().strftime("%Y-%m-%d")
    batches = get_batch_name(students)
    overall = analyze_batch(students)

    with open(filename, "w")as f:
        # Header
        f.write(f"# Institura Analytics Dashboard\n")
        f.write(f"**Generated:** {today}\n")
        f.write(f"**Total Students:** {overall["total"]}\n\n")


        # Overall analysis
        f.write("## Overall Performance\n")
        f.write(f"- Average Marks: {overall["average"]}\n")
        f.write(f"- Topper: {overall["topper"]} ({overall["topper_marks"]} marks)\n")
        f.write(f"- Pass: {overall["pass_count"]} | Fail: {overall["fail_count"]}\n")
        f.write(f"- Fee Paid: {overall["paid_count"]} | Pending: {overall["pending_count"]}\n")\

        # Per batch Analysis
        f.write("## Batch-wise Analysis\n")
        for batch in batches:
            batch_students = filter_by_batch(students, batch)
            batch_analysis = analyze_batch(batch_students)
            f.write(f"\n## {batch}\n")
            f.write(f"- Students: {batch_analysis["total"]}\n")
            f.write(f"- Average: {batch_analysis["average"]}\n")
            f.write(f"- Topper: {batch_analysis["topper"]}\n")
            f.write(f"- Pass: {batch_analysis["pass_count"]} | Fail: {batch_analysis["fail_count"]}\n")

        #Student Detail Table
        f.write("\n## Student Details\n")
        f.write("| Name | Batch | Marks | Status | Fee |\n")
        f.write("|------|-------|-------|--------|-----|\n")
        for s in sorted(students, key=lambda s: s.marks, reverse=True):
            status ="Pass" if s.marks>=40 else "Fail"
            f.write(f"| {s.name} | {s.batch} | {s.marks} | {status} | {s.fee_status} |\n")

    print(f"Report Saved to {filename}")

if __name__ == "__main__":
    from data import load_students
    students = load_students("sample_students.csv")
    generate_report(students)


        




