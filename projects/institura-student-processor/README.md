# Institura Student Processor

Institura is an AI platform that helps coaching institutes
with analytics and student management. This tool is one part
of that system — a CLI application that processes student data,
analyzes batch performance, and generates professional reports.

Built with pure Python in 5 days as part of my 28-week
Python for AI Automation journey.

## What This Tool Does

- Reads student data from CSV files
- Cleans messy data — fixes names, converts marks,
  handles missing fields gracefully
- Analyzes batch performance — topper, average marks,
  pass/fail count, fee collection status
- Filters students by batch (IIT-JEE, NEET, etc.)
- Generates a professional text report file

## Who Is This For

Institute owners and administrators who want to see
student performance data at a glance — without opening
Excel or waiting for someone to prepare a report manually.

## How To Run

git clone https://github.com/ashishpratapsai/python-for-ai
cd projects/institura-student-processor
python3 main.py

## Project Structure

institura-student-processor/
├── main.py               — terminal menu, entry point
├── processor.py          — all functions, brain of the tool
├── sample_students.csv   — sample data with real Institura fields
├── institura_report.txt  — generated report output
└── README.md

## What I Learned

The hardest part was not writing the code — it was thinking
through the data flow. How messy real-world data needs to be
cleaned before analysis. How functions connect in a pipeline.
How one file imports from another using modules.

Every concept from Days 1-21 of my Python journey was used
here — functions, loops, dictionaries, error handling,
file I/O, and terminal menus with while loops.

## Built With

Pure Python — zero external libraries
Part of my 28-week Python for AI Automation series
YouTube: [\[your channel link\]](https://www.youtube.com/@AutomatewithAshish)
GitHub: https://github.com/ashishpratapsai/python-for-ai