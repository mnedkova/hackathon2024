from bs4 import BeautifulSoup
import requests
import json
from datetime import datetime


#base_url = (f"https://umassdining.com/foodpro-menu-ajax?tid={id}&date=")
org_url = requests.get('https://umassdining.com/locations-menus/worcester/menu')
soup = BeautifulSoup(org_url.content, 'html.parser')

select_me = soup.find('select',{'id': 'upcoming-foodpro'}) #select menu
tid = {1: "Worcester",
       2: "Franklin",
       3: "Hampshire",
       4: "Berkshire"
       }


def parseResponse(date_val, location_name, location_id, content):
    # print(content)
    json_file = json.loads(content)
    
    new_date = datetime.strptime(date_val,"%m/%d/%Y").strftime("%Y-%m-%d")
    
    doc = {
        "date": new_date,
        "location": location_name,
        "id": f'{date_val}-{location_id}',
    }
    
    doc_meals = []
    for meals in json_file:
        # print(json_file[key])
        for category in json_file[meals]:
            # print(category)
            
            dishes_html = BeautifulSoup(json_file[meals][category], 'html.parser')
            dishes = dishes_html.findAll("a")
            # dish = jsonsoup.get_text('menu-category-name')
            # if dish:
            #     print("THERE IS A DISH")
            for dish in dishes:
                dishes_for_each_meal = {
                    "meal": meals,
                    "category": category,
                    "food": dish.get_text() 
                }
                doc_meals.append(dishes_for_each_meal)
    doc["meals"] = doc_meals
    return doc



if select_me:
    opt = select_me.find_all('option') #option tag
    #extracts data from each option
    for location_id, location_name in tid.items(): #iterating through the dining halls
            # Construct the URL with the correct tid for each location
            base_url = (f"https://umassdining.com/foodpro-menu-ajax?tid={location_id}&date=")
            print(f"Fetching menu for {location_name}")
            
            # You can now send a request to the constructed URL
            response = requests.get(base_url)
            #Set to 14
            MAX_DAYS = 1
            for options in range(MAX_DAYS): #amount of days 1-14 (13 days ahead?)
                    date_val = opt[options]['value'] #the date 11/10/2024 format
                    r = requests.get(f'{base_url}{date_val}')
                    day = BeautifulSoup(r.content, 'html.parser')
                    
                    doc = parseResponse(date_val, location_name, location_id, r.content)
                    new_date = datetime.strptime(date_val,"%m/%d/%Y").strftime("%Y-%m-%d")
                    file_name = f'{new_date}-{location_name}.json'
                    print(file_name)
                    print(type(date_val))
                    with open(file_name, 'w') as fp:
                        json.dump(doc, fp)
