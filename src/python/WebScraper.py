#%%
from selenium import webdriver
import json

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
options.headless = True # do not open the browser 
options.binary_location = "/usr/bin/brave-browser-stable" # set path to browser file
driver = webdriver.Chrome(executable_path="/home/fedmag/Projects/TwitchDotaHelper/chromedriver", options=options)

def retrieve_data(hero_name): 
    hero_abilities = []
    print("------------ Working on: {}".format(hero_name))
    driver.get("https://www.dotabuff.com/heroes/{}/abilities".format(hero_name))
    sections = driver.find_elements_by_tag_name("section")
    sections = sections[2:]
    for section in sections:
        raw_string = section.text
        hero_abilities.append(raw_string)
    heroes_dict[hero_name] = hero_abilities
    hero_abilities = []


heroes_dict = {}
hero_names = []
with open("/home/fedmag/Projects/TwitchDotaHelper/data/heroes.txt", "r") as file:
    print("Retrieving heroes list...")
    lines = file.readlines()
    for name in lines:
        hero_names.append(name.replace("\n",""))
    print("..done!")

for hero in hero_names:
    retrieve_data(hero)
json_heroes = json.dumps(heroes_dict)

with open ("/home/fedmag/Projects/TwitchDotaHelper/data/WebScraper.json", 'w') as file:
    file.write(json_heroes)
    print("File successfully created!")



driver.close()
# %%
