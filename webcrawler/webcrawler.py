from selenium import webdriver
from bs4 import BeautifulSoup

import json

cService = webdriver.ChromeService(executable_path='D:/Selenium/chromedriver.exe')
driver = webdriver.Chrome(service=cService)

driver.get("https://www.serebii.net/pokemongo/previousraidbattles.shtml")

html = driver.page_source

soup = BeautifulSoup(html, 'html.parser')

ul_element = soup.find('div', {'id': 'anonymous_element_312'}).find('ul')
li_elements = ul_element.find_all('li')

data_dict = {}

for li in li_elements:
    title = li.get("title")
    tables = li.find_all('tr')

    # print(tables[2].get_text(strip=True))

    listIndex = 0
    sub_dict = {}

    for table in tables: 
        content = table.get_text(strip=True)

        if content != "" and content[0] == "#":
            sub_dict[listIndex] = [content]
            listIndex+=1

    data_dict[title] = sub_dict


with open("data.json", 'w') as json_file:
    json.dump(data_dict, json_file, indent=4)

driver.quit()
