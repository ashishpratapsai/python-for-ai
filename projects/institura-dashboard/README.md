# Institura Analytics Dashboard

A CLI analytics tool for coaching institutes that reads student 
CSV data and generates a professional performance report.

Built with pure Python as part of my 28-week 
Python for AI Automation journey — Phase 2.

## What This Tool Does

- Loads student data from CSV using Pydantic validation
- Shows overall institute performance at a glance
- Breaks down results batch-wise (IIT-JEE vs NEET)
- Tracks fee collection — paid vs pending
- Finds the topper, pass/fail counts, average marks
- Generates a clean markdown report sorted by performance

## How To Run

git clone https://github.com/ashishpratapsai/python-for-ai
cd projects/institura-dashboard

python3 main.py

## Phase 2 Concepts Used

- Pydantic — automatic data validation and cleaning
- Type hints — every function is fully typed
- Logging — professional logging replacing print()
- pathlib — safe file path handling
- csv.DictReader — reads CSV rows as dictionaries
- List comprehensions — batch filtering and analysis
- Dot notation — Pydantic models use student.name not student["name"]

## Project Structure

institura-dashboard/
├── main.py          — entry point
├── data.py          — Pydantic Student model + CSV loader
├── analyzer.py      — batch analysis, fee tracking
├── reporter.py      — markdown report generator
├── sample_students.csv
└── README.md

## Phase 1 vs Phase 2

Phase 1 used manual try/except for cleaning and print() everywhere.
Phase 2 uses Pydantic for automatic validation and logging for
professional output tracking.

## Built With

Pure Python — Pydantic, pathlib, csv, logging
Part of my 28-week Python for AI Automation series
YouTube: https://www.youtube.com/@AutomatewithAshish
GitHub: https://github.com/ashishpratapsai/python-for-ai