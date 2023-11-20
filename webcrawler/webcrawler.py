from selenium import webdriver
from bs4 import BeautifulSoup

cService = webdriver.ChromeService(executable_path='D:/Selenium/chromedriver.exe')
driver = webdriver.Chrome(service=cService)

driver.get("https://www.serebii.net/pokemongo/previousraidbattles.shtml")

html = driver.page_source

soup = BeautifulSoup(html, 'html.parser')

ul_element = soup.find('div', {'id': 'anonymous_element_312'}).find('ul')

li_elements = ul_element.find_all('li')

for li in li_elements:
    title = li.get("title")
    print(title)

    tables = li.find_all('td')
    for table in tables:
        content = table.get_text(strip=True)
        print(content)

driver.quit()
