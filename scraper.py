import requests
from bs4 import BeautifulSoup
import pandas as pd

# Website URL
url = "https://books.toscrape.com"

# Download the webpage
response = requests.get(url)

# Read the webpage
soup = BeautifulSoup(response.text, "html.parser")

# Find all books
books = soup.find_all("article")

# Empty list to store data
data = []

# Loop through each book
for book in books:

    # Get title
    title = book.h3.a["title"]

    # Get price
    price = book.find("p", class_="price_color").text

    # Get rating
    rating = book.find("p")["class"][1]

    # Store the data
    data.append([title, price, rating])

# Create a table
df = pd.DataFrame(data, columns=["Title", "Price", "Rating"])

# Save as CSV
df.to_csv("books.csv", index=False, encoding="utf-8-sig")

print("Data saved successfully!")