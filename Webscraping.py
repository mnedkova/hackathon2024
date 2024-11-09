from bs4 import BeautifulSoup
from datetime import date
import requests
 
"""Pages we want to scrape:
https://umassdining.com/foodpro-menu-ajax?tid=1&date=11/09/2024
"""


day = date.today()

month = date.month()

year = date.year()


page_to_scrape = requests.get("https://quotes.toscrape.com/")
soup = BeautifulSoup(page_to_scrape.text, "html.parser")
quotes = soup.findAll("")



