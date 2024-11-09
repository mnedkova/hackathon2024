from bs4 import BeautifulSoup
import requests


#base url usin ajax 
base_url = 'https://umassdining.com/foodpro-menu-ajax?tid=1&date='



org_url = requests.get('https://umassdining.com/locations-menus/worcester/menu')
soup = BeautifulSoup(org_url.content, 'html.parser')

select_me = soup.find('select',{'id': 'upcoming-foodpro'})
if select_me:
    opt = select_me.find_all('option')
    #extracts data from each option 
    for options in opt:
        dat_val = options['value']
    # prints the dates
        print(f"Menu for date {dat_val}")
    #requests for each date that we get
        r = requests.get(f'{base_url}{dat_val}')
        day = BeautifulSoup(r.content, 'html.parser')

        food_items = day.find_all('li')
        
        #allows us to get the food from the menu
        soup = BeautifulSoup(r.content, 'html.parser')
        dish_name = soup.find_all('a', {'data-dish-name':True})

        for dish in dish_name:
            name = dish.get('data-dish-name')
            if name:
                ##!!! Issue: printing only the first word of the food name in the menu

                ##I have no idea what is causing the issue for only one word to print
                print(f"Dish: {name.strip()}")
        
        print()


