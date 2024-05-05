# Web Scraper Template. Readme at the bottom of the code!

from bs4 import BeautifulSoup
import requests

#### Function 'scrapesite' is used to define the variables associated with the data we want to scrape.

def scrapeSite():
    pagetoscrape = requests.get("https://www.tapaway.com.au/blog")
    soup = BeautifulSoup(pagetoscrape.text, "html.parser")
    authors = soup.findAll('span', attrs={'class':'tQ0Q1A'})
    titles = soup.findAll('p', attrs={'class':'bD0vt9 KNiaIk'})
    views = soup.findAll('span', attrs={'class':'eYQJQu'})

    #### for statement utilises the zip functionality to use and pull information fromm multiple variables and combine them into one for statement.
    
    for author, title, view in zip(authors, titles, views):
        print(author.text + " - " + title.text + " - Views: " + view.text)

scrapeSite()


# Web Scraper Template
# This Python script provides a basic template for web scraping using BeautifulSoup, a library for parsing HTML and XML documents.
#
# How to Use
# Installation: Make sure you have Python installed on your system. You can download it from Python's official website. Additionally, you need to install the BeautifulSoup library. You can do this via pip, the package installer for Python. Open your terminal or command prompt and type:
#
# Ensure the library and modules required are installed:
#
# Inside your terminal copy and paste the following lines -
#
# pip3 install bs4
#
# pip3 install requests
#
# Understanding the Code:
#
# >> from bs4 import BeautifulSoup: << This line imports the BeautifulSoup class from the bs4 library, which we'll use for parsing HTML.
#
# >> import requests: << This line imports the requests library, which allows us to send HTTP requests easily.
#
# >> def scrapeSite(): << This function defines the scraping process. It sends a request to the specified URL, extracts relevant information from the HTML using BeautifulSoup, and prints it out.
#
#       Inside scrapeSite(): We define the URL of the page we want to scrape. Then, we use BeautifulSoup to parse the HTML content of the page and find specific elements using their HTML tags and class attributes.
#
# Customization: You can modify the pagetoscrape variable to point to any URL you want to scrape. Additionally, you can adjust the elements you want to extract by modifying the findAll() method calls.
#
# Running the Script: After modifying the script according to your needs, you can run it by executing the Python file. Open your terminal or command prompt, navigate to the directory containing the script, and type:
#
# Copy code
# python your_script_name.py
# Replace your_script_name.py with the name of your Python script file.
#
# Additional Notes
# This template is designed for educational purposes to help you understand the basics of web scraping. When scraping websites, make sure to review their terms of service and robots.txt file to ensure compliance with their policies.
#
# Experiment with different websites and data elements to enhance your understanding of web scraping and BeautifulSoup.
#
# Happy coding!