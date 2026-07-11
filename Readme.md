# 📚 CodeAlpha - Web Scraping Project

## 📌 Project Overview

This project was completed as part of the **CodeAlpha Data Analytics Internship**.

The objective of this project is to collect book information from a website using **Python Web Scraping** techniques. The program automatically extracts book details such as title, price, and rating from the website **Books to Scrape** and stores the extracted data in a CSV file for further analysis.

---

## 🎯 Project Objectives

* Learn the fundamentals of Web Scraping.
* Extract data from a real website using Python.
* Store scraped data in a structured CSV file.
* Build a beginner-friendly data collection project.

---

## 🌐 Website Used

https://books.toscrape.com

> This website is created specifically for practicing web scraping.

---

## 📂 Project Structure

```
CodeAlpha_WebScraping/
│
├── data/
│   └── books.csv
│
├── screenshots/
│   ├── website.png
│   ├── code.png
│   ├── terminal_output.png
│   ├── excel_output.png
│   └── README.md
│
├── scraper.py
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

---

## 🛠 Technologies Used

* Python
* Requests
* BeautifulSoup4
* Pandas
* VS Code

---

## 📦 Python Libraries

```
requests
beautifulsoup4
pandas
```

Install them using:

```bash
pip install -r requirements.txt
```

---

## ▶️ How to Run the Project

1. Clone this repository.

2. Install the required libraries.

```bash
pip install -r requirements.txt
```

3. Run the scraper.

```bash
python scraper.py
```

4. After successful execution, a file named **books.csv** will be created inside the **data** folder.

---

## 📊 Output

The scraper extracts:

* Book Title
* Book Price
* Book Rating

The collected data is stored in:

```
data/books.csv
```

---

## 📷 Project Screenshots

Project screenshots are available in the **screenshots** folder.

---

## 📚 What I Learned

* Basics of Web Scraping
* Sending HTTP requests
* Reading HTML using BeautifulSoup
* Extracting required information
* Working with CSV files using Pandas
* Organizing a professional GitHub repository

---

## 🚀 Future Improvements

* Scrape all 50 pages instead of only the first page.
* Save data into an Excel (.xlsx) file.
* Add book availability information.
* Perform Exploratory Data Analysis (EDA) on the collected dataset.

---

## 👩‍💻 Author

**Akella Lakshmi Aiswarya**

B.Tech CSE (AI & ML)

CodeAlpha Data Analytics Intern
