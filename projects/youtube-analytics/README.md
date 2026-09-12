# YouTube Analytics Fetcher

A CLI tool that fetches your YouTube channel data via the 
YouTube Data API and generates a weekly analytics report 
in markdown format.

Built with pure Python as part of my 28-week 
Python for AI Automation journey.

## What This Tool Does

- Fetches your channel overview — subscribers, total views, video count
- Gets your latest 10 videos with views, likes, and comments
- Finds your best performing video by views
- Calculates average views and likes across latest videos
- Generates a clean markdown report you can save and share

## Who Is This For

YouTubers who want a quick weekly snapshot of their channel 
performance without manually checking YouTube Studio for 
each video.

## How To Run

git clone https://github.com/ashishpratapsai/python-for-ai
cd projects/youtube-analytics

# Add your credentials
cp .env.example .env
# Edit .env with your YouTube API key and Channel ID

pip install httpx python-dotenv
python3 main.py

## Project Structure

youtube-analytics/
├── main.py        — entry point, connects everything
├── fetcher.py     — YouTube API calls
├── analyzer.py    — finds best video, calculates averages
├── reporter.py    — generates markdown report
├── .env.example   — template for credentials
└── README.md

## What I Learned

Building this taught me how to read API documentation,
make HTTP requests with httpx, parse nested JSON responses,
and organize code across multiple files as a proper package.
The YouTube API needs two separate calls — search for video
IDs, then videos endpoint for detailed stats.

## Built With

Pure Python — httpx, python-dotenv
YouTube Data API v3
Part of my 28-week Python for AI Automation series
YouTube: https://www.youtube.com/@AutomatewithAshish
GitHub: https://github.com/ashishpratapsai/python-for-ai