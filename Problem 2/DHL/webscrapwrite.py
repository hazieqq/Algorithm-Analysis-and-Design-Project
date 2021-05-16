from selenium import webdriver
from bs4 import BeautifulSoup
from collections import Counter
import re
import os
#5 (a)
try:
    PATH = "Problem 2\chromedriver.exe"
    URL = "https://themalaysianreserve.com/2017/03/31/city-link-targets-20-revenue-growth-with-new-super-hub/"
    driver = webdriver.Chrome(PATH)
    savePath = 'Problem 2\Citylink\Article 1'
    fileName1 = "sample.txt"
    fileName2 = "data.txt"
    sampleText = os.path.join(savePath, fileName1)
    dataText = os.path.join(savePath, fileName2)

    driver.get(URL)

    text_file = open(sampleText, "w")

    page = driver.page_source
    page_soup = BeautifulSoup(page, 'html.parser')

    article = page_soup.find('section', attrs={'class': 'single-post-content clearfix'})#class="navigation-top pb-30 pt-20" id="vuukle-powerbar" class="single-post-content clearfix"

    for p in article.find_all('p'):
        n = text_file.write(p.text + "\n")

    # 5(b)

    text_file = open(sampleText, "r")
    wordstring = text_file.read()
    wordstring = wordstring.lower()
    wordstring = wordstring.replace('"', "")
    wordlist = re.findall(r"[\w&']+", wordstring)
    print(wordlist)
    # remove duplicate & print to text file

    output = open(dataText, "w")
    c = Counter(wordlist)
    a = list(c.values())
    b = list(c.keys())
    for i in range(len(a)):
        # print('{},{}'.format(b[i], a[i]))
        output.write('{},{}'.format(b[i], a[i])+"\n")

    output.close()
    text_file.close()
    driver.close()
except FileNotFoundError:
    print("file not found")