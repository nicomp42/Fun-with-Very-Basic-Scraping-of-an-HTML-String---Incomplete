# Fun with Very Basic Scraping of an HTML String - Incomplete
# main.py

from utilsPackage.utils import *
import bs4

# Just load the contents of an HTML file into a Python string
HTML = getHTML()

# Parse the HTML into something we can search
soup = bs4.BeautifulSoup(HTML, 'html.parser')

#print(soup)
# Find all the spans, regardless of where they are on the page
    
# Find only the spans assigned the class "mySpanClass"


# Find the Table Data (td) containers
