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
    #requests for each date that we get 
        r = requests.get(f'{base_url}{dat_val}')
        day = BeautifulSoup(r.content, 'html.parser')

        food_items = day.find_all('li')
        print(f"Menu for date {dat_val}")

        soup = BeautifulSoup(r.content, 'html.parser')
        dish_name = soup.find_all('a')

        for dish in dish_name:
            name = dish.get('data-dish-name')
            if name:
                print(f"Dish: {name}")
        
        print()
