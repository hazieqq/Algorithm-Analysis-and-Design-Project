from selenium import webdriver
from bs4 import BeautifulSoup, NavigableString

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.nst.com.my/news/nation/2021/02/663907/violent-sorting-parcels-jt-apologises-customers")

text_file = open("sample.txt", "w")
# n = text_file.write('haha to pythonexamples.org')
# text_file.close()

page = driver.page_source
page_soup = BeautifulSoup(page,'html.parser')

article = page_soup.find('div',attrs={'class':'field field-body'}) 
# print(article.text)

for p in article.find_all('p'):
    if isinstance(p, NavigableString):
        continue
    n = text_file.write(p.text + "\n")
    print(p.text)

text_file.close()
