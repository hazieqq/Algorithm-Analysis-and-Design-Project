from selenium import webdriver
from bs4 import BeautifulSoup, NavigableString
from collections import Counter
import re
#5 (a)
try:
    PATH = "Problem 2\chromedriver.exe"
    driver = webdriver.Chrome(PATH)

    driver.get(
        "https://www.nst.com.my/news/nation/2021/02/663907/violent-sorting-parcels-jt-apologises-customers")

    text_file = open("sample.txt", "w")

    page = driver.page_source
    page_soup = BeautifulSoup(page, 'html.parser')

    article = page_soup.find('div', attrs={'class': 'field field-body'})

    for p in article.find_all('p'):
        n = text_file.write(p.text + "\n")

    # 5(b)

    text_file = open("sample.txt", "r")
    wordstring = text_file.read()
    wordstring = wordstring.lower()
    wordstring = wordstring.replace('"', "")
    wordlist = re.findall(r"[\w&']+", wordstring)

    # remove duplicate & print to text file

    output = open("data.txt", "w")
    c = Counter(wordlist)
    a = list(c.values())
    b = list(c.keys())
    for i in range(len(a)):
        print('{},{}'.format(b[i], a[i]))
        output.write('{},{}'.format(b[i], a[i])+"\n")

    output.close()
    text_file.close()
    driver.close()
except FileNotFoundError:
    print("file not found")
