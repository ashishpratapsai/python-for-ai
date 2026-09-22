# Transcript-to-Tutorial Generator

Converts a YouTube transcript into a structured written tutorial
using the Anthropic Claude API.

## What It Does

Feed it any YouTube transcript and get back a professional
markdown tutorial with sections, code blocks, key takeaways,
and a thumbnail prompt. What takes 2 hours to write manually
takes 30 seconds.

## Real Use Case

Every YouTube video I make on Automate With Ashish becomes a
blog post, LinkedIn article, and newsletter issue automatically.
Same content. Zero extra writing. 3x the reach.

## How It Works

1. Reads transcript from `sample_transcript.txt`
2. Claude extracts structure using tool use (guaranteed clean output)
3. Outputs formatted markdown to `tutorial.md`

## Setup

pip install anthropic python-dotenv

Create .env file:
ANTHROPIC_API_KEY=your_key_here

## Run

python3 main.py

## Output

A `tutorial.md` file with:
- Title
- Introduction
- Sections with headings and code blocks
- Key takeaways
- Thumbnail prompt for YouTube

## Built With

Python, Anthropic Claude API, Pydantic, Prompt Caching, Tool Use

Part of my 28-week Python for AI Automation series.
YouTube: https://www.youtube.com/@AutomatewithAshish
GitHub: https://github.com/ashishpratapsai/python-for-ai