from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome('chromedriver.exe')

url = "https://gall.dcinside.com"

driver.get(url)

soup = BeautifulSoup(driver.page_source, 'html.parser')

driver.quit()

content = soup.select_one("#categ_listwrap").select("li > a")

f = open("data_name.txt", 'w')

for i in content:
    print(i.text, i["href"].replace("/lists/", "/write/"))
    f.write(i.text + " " + i["href"].replace("/lists/", "/write/") + "\n")

