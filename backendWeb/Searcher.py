import json
#Ask user for input
foodName = input("What do you desire: ")

#gets the json file with dining hall and food
with open('2024-11-09-Worcester.json', 'r') as file:
    data = json.load(file)

#gets the date and location
date = data["date"]
location = data["location"]

#parses through the file
for item in data["meals"]:
    if item["food"].lower() == foodName.lower():
         print(f"Durimg {item['meal']} there is {foodName} in {location} on {date}.")
           


