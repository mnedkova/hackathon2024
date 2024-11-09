from bs4 import BeautifulSoup
from datetime import date
import requests
 
"""Pages we want to scrape:
https://umassdining.com/foodpro-menu-ajax?tid=1&date=11/09/2024
"""


day = date.today()

month = date.month()

year = date.year()


page_to_scrape = requests.get("https://umassdining.com/locations-menus/worcester/menu")
soup = BeautifulSoup(page_to_scrape.text, "html.parser")
quotes = soup.findAll("li", attrs = {"class":"lightbox-nutrition"})
#authors = soup.findAll("small", attrs={"class":"author"})

#file = open("scraped_quotes.csv", "w")
#writer = csv.writer(file)

#writer.writerow(["Food"])


"""for quote, author in zip(quotes, authors):
    print(quote.text + " , " + author.text)
    writer.writerow([quote.text,author.text])
file.close()"""

for a in quotes:
    print(a.text)








