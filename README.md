# Day-3_Python_Developer-Internship_Task-3
This is a beginner-friendly Python project that scrapes top news headlines from a news website (BBC News) and saves them into a `.txt` file.
# 📰 News Headlines Web Scraper

This is a beginner-friendly Python project that scrapes top news headlines from a news website (BBC News) and saves them into a `.txt` file.

## 🎯 Objective

Automate data collection from a public website using Python.

## 🛠 Tools & Libraries Used

- Python
- requests
- BeautifulSoup (from `bs4`)

## 🚀 How It Works

1. Sends a request to the BBC News homepage.
2. Parses the HTML content using BeautifulSoup.
3. Extracts all news headlines found in `<h2>` and `<h3>` tags.
4. Saves the headlines in a `headlines.txt` file.

## 📦 Requirements

Make sure you have Python installed.

Install dependencies:
```bash
pip install requests beautifulsoup4
python news_scraper.py

-------------------------
1. Climate change: UN issues global warning
2. US election: Biden and Trump prepare for debate
3. India launches new moon mission
...
