# Web Scraping ETL Pipeline with SQLite

## Project Overview

Web Scraping ETL Pipeline with SQLite is a Python automation project that collects sample quote data from a public website, cleans and transforms the extracted records, stores the structured data into a SQLite database, and exports the final result to a CSV file.

This project demonstrates a basic Data Engineering workflow using the ETL process:

* **Extract**: Collect data from web pages
* **Transform**: Clean and structure the extracted data
* **Load**: Save the processed data into SQLite and export it to CSV

The project is designed to show how Python can automate repetitive data collection tasks and organize information for easier analysis.

---

## Key Features

* Scrapes quote data from multiple web pages
* Extracts quote text, author name, and tags
* Cleans and transforms raw scraped data
* Stores structured records in a SQLite database
* Avoids duplicate records when loading data
* Exports processed data to a CSV file
* Uses a simple modular Python project structure
* Demonstrates a beginner-friendly ETL workflow

---

## Technologies Used

* Python
* Requests
* BeautifulSoup
* SQLite
* CSV
* Web Scraping
* Data Processing

---

## Project Structure

```text
web-scraping-etl-pipeline-with-sqlite/
│
├── main.py
├── config.py
├── extractor.py
├── transformer.py
├── loader.py
├── requirements.txt
├── README.md
│
├── data/
│   └── quotes_export.csv
│
└── database/
    └── quotes.db
```

---

## File Description

### `main.py`

The main entry point of the project.
It controls the full ETL workflow:

1. Checks or creates the database
2. Scrapes quote data from the website
3. Cleans and transforms the data
4. Saves the records into SQLite
5. Exports the final dataset to CSV

---

### `config.py`

Stores project configuration values such as:

* Website URL
* Number of pages to scrape
* Database path
* CSV export path

This makes the project easier to update without changing the main logic.

---

### `extractor.py`

Handles the **Extract** step of the ETL process.

It sends requests to the target website, reads the HTML content, and extracts quote-related data such as:

* Quote text
* Author
* Tags

---

### `transformer.py`

Handles the **Transform** step.

It cleans and prepares the extracted records before saving them.
This step helps make the data more consistent and ready for storage or analysis.

---

### `loader.py`

Handles the **Load** step.

It saves the processed data into a SQLite database and exports the final dataset to a CSV file.

---

## How It Works

```text
Start program
↓
Check or create SQLite database
↓
Scrape quote data from multiple web pages
↓
Extract quote text, author, and tags
↓
Clean and transform records
↓
Insert processed records into SQLite database
↓
Export data to CSV
↓
Process completed
```
