from datetime import datetime


def save_report(results:dict, output_file:str="summaries.md")-> None:
    with open(output_file,"w") as f:
        f.write(f"# Institura Parent Summaries\n**Generated**  {datetime.now().strftime('%Y-%m-%d')}\n\n")

        for student_id, message in results.items():
            f.write(f"## {student_id}\n\n")
            f.write(f"{message}\n\n")

        print(f"Report saved to {output_file}")