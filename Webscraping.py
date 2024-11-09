from bs4 import BeautifulSoup
import requests
import csv

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








