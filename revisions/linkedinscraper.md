# LinkedIn Job Scraper: Detailed Guide

This guide will walk you through recreating the LinkedIn job scraper for your own project. We'll cover the structure, key components, and how to set up and use the scraper.

## 1. Project Structure

Your project should have the following structure:

linkedin_scraper/
│
├── main.py
├── config.json
├── requirements.txt
├── static/
│ └── job_actions.js
└── README.md

## 2. Dependencies

Create a `requirements.txt` file with the following content:

requests
beautifulsoup4
pandas
langdetect

Install the dependencies using:

pip install -r requirements.txt

## 3. Configuration (config.json)

Create a `config.json` file to store your scraper settings:

json
{
"search_queries": [
{
"keywords": "software engineer",
"location": "United States",
"f_WT": "2"
}
],
"pages_to_scrape": 5,
"rounds": 1,
"timespan": "r604800",
"days_to_scrape": 7,
"db_path": "jobs.db",
"jobs_tablename": "jobs",
"filtered_jobs_tablename": "filtered_jobs",
"headers": {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
},
"proxies": {},
"languages": ["en"],
"desc_words": ["senior", "lead"],
"title_exclude": ["senior", "manager"],
"title_include": ["engineer", "developer"],
"company_exclude": []
}


Adjust these settings according to your needs.

## 4. Main Scraper Script (main.py)

The `main.py` file contains the core scraping logic. Here's a breakdown of its key components:

### 4.1 Import necessary libraries

python
import requests
import json
import sqlite3
import sys
from bs4 import BeautifulSoup
import time as tm
from itertools import groupby
from datetime import datetime, timedelta, time
import pandas as pd
from urllib.parse import quote
from langdetect import detect
from langdetect.lang_detect_exception import LangDetectException


### 4.2 Helper functions

Implement these helper functions:

- `load_config(file_name)`: Load the configuration from JSON file
- `get_with_retry(url, config, retries=3, delay=1)`: Make HTTP requests with retry logic
- `transform(soup)`: Parse job information from HTML
- `transform_job(soup)`: Extract job description from individual job pages
- `safe_detect(text)`: Safely detect language of text
- `remove_irrelevant_jobs(joblist, config)`: Filter out irrelevant jobs
- `remove_duplicates(joblist, config)`: Remove duplicate job listings
- `convert_date_format(date_string)`: Convert date strings to date objects
- `create_connection(config)`: Create a SQLite database connection
- `create_table(conn, df, table_name)`: Create a new table in the database
- `update_table(conn, df, table_name)`: Update existing table with new records
- `table_exists(conn, table_name)`: Check if a table exists in the database
- `job_exists(df, job)`: Check if a job already exists in the dataframe

### 4.3 Main scraping functions

Implement these core scraping functions:

- `get_jobcards(config)`: Scrape job cards from search results pages
- `find_new_jobs(all_jobs, conn, config)`: Find jobs that are not already in the database

### 4.4 Main function

The `main(config_file)` function orchestrates the entire scraping process:

1. Load configuration
2. Scrape job cards
3. Filter out existing jobs
4. Scrape detailed job descriptions
5. Apply filters and remove irrelevant jobs
6. Store results in the database and CSV files

### 4.5 Script execution

Add this at the end of the file to allow running the script with a custom config file:

python
if name == "main":
config_file = 'config.json' # default config file
if len(sys.argv) == 2:
config_file = sys.argv[1]
main(config_file)


## 5. Job Actions (static/job_actions.js)

This JavaScript file likely contains frontend logic for interacting with the scraped job data. Implement functions for displaying, filtering, and managing job listings in your web interface.

## 6. Usage

1. Set up your `config.json` file with desired search parameters and settings.
2. Run the scraper:
   ```
   python main.py
   ```
   Or with a custom config file:
   ```
   python main.py custom_config.json
   ```
3. The script will scrape job listings, store them in a SQLite database, and export them to CSV files.

## 7. Customization

To adapt this scraper for other websites:

1. Modify the URL structure in `get_jobcards()` to match the target website's API or search results page.
2. Update the `transform()` and `transform_job()` functions to parse the HTML structure of the new website.
3. Adjust the configuration options in `config.json` to match the new website's search parameters and filtering options.
4. Update any website-specific headers or request parameters in the `get_with_retry()` function.

## 8. Ethical Considerations

- Always respect the website's robots.txt file and terms of service.
- Implement appropriate delays between requests to avoid overloading the server.
- Consider using official APIs if available, rather than scraping.

## 9. Maintenance

Regularly check and update your scraper to accommodate any changes in the website's structure or API. Web scraping is inherently fragile, so be prepared to make adjustments as needed.

By following this guide, you should be able to recreate and customize the LinkedIn job scraper for your own projects or adapt it to scrape job listings from other websites.