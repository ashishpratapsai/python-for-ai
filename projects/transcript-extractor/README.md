# Transcript Extractor

A CLI tool for YouTube creators that automatically finds
key moments in video transcripts based on topics you care about.

Feed it a transcript. Get back only the sentences that matter.

Built with pure Python as part of my 28-week
Python for AI Automation journey.

## What This Tool Does

- Reads any YouTube transcript from a text file
- Finds key moments — sentences containing your keywords
- Shows how many key moments were found
- Saves a clean markdown summary you can use for
  chapters, shorts, or blog posts

## Who Is This For

YouTube creators who want to find the most important
moments in their videos without reading the entire
transcript manually.

## How To Run

git clone https://github.com/ashishpratapsai/python-for-ai
cd projects/transcript-extractor
python3 main.py

## Default Keywords

Claude Code, AI agents, n8n, automation, MCP, Python

Change these in main.py to match your channel topics.

## Project Structure

transcript-extractor/
├── main.py                  — terminal menu, entry point
├── extractor.py             — all functions, brain of the tool
├── sample_transcript.txt    — sample YouTube transcript
├── transcript_summary.md    — generated markdown summary
└── README.md

## What I Learned

Every YouTube creator has the same problem — long transcripts,
no easy way to find the key moments. Python solved it in
three functions and 50 lines of code.

This project used concepts from Days 1-23:
functions, loops, file I/O, list comprehension,
any() for keyword matching, and terminal menus.

## Built With

Pure Python — zero external libraries
Part of my 28-week Python for AI Automation series
GitHub: https://github.com/ashishpratapsai/python-for-ai