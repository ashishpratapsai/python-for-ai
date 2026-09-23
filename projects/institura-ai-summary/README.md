# Institura AI Parent Summary

Generates personalized parent messages for all students in one
batch API call. Feed it a CSV of student data — get back
professional summaries tailored to each student's performance
and fee status. 500 students in under 5 minutes at half the
normal API cost.

## What It Does

- Reads student data from CSV with automatic data cleaning
- Submits all students as one batch to Claude API (50% cheaper)
- Adjusts tone automatically — encouraging for high marks,
  constructive for average, urgent for low marks
- Adds fee reminder only when payment is pending
- Saves all summaries to a markdown report

## Real Impact

Built for Institura — a live SaaS for coaching institutes.
What took 30-60 minutes of manual writing per batch now takes
5 minutes for any number of students.

## Setup

pip install anthropic python-dotenv pydantic

Create .env:
ANTHROPIC_API_KEY=your_key_here

## How to Run

Step 1 — Submit batch:
python3 main.py

Step 2 — Wait 5 minutes, then get results:
python3 main.py --check

Output saved to summaries.md

## Project Structure

models.py    — Pydantic models with data validation
data.py      — loads and cleans students.csv
generator.py — batch API submit and results retrieval
reporter.py  — saves summaries to markdown
main.py      — CLI entry point with --check flag

## Sample Output

Sneha Singh (96/100) — celebratory, proud tone
Rahul Sharma (85/100) — encouraging, commendable tone
Amit Kumar (35/100) — urgent + fee reminder included

## Built With

Python, Anthropic Claude API, Batch Processing, Pydantic

Part of my 28-week Python for AI Automation series.
YouTube: https://www.youtube.com/@AutomatewithAshish
GitHub: https://github.com/ashishpratapsai/python-for-ai