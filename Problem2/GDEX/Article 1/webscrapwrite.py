from io import IncrementalNewlineDecoder
from selenium import webdriver
from bs4 import BeautifulSoup
from collections import Counter
import re
import os
from swprogram import excludeStopw
from posWordScraper import positive
from negWordScraper import negative
from neutralWord import neutral
from calculate import calc
from posWordGraph import posGraph
from negWordGraph import negGraph
from posNegWordGraph import PosNegGraph
from wordCountGraph import CountGraph

from Article2 import webscrapwrite2
from Article3 import webscrapwrite3

#5 (a)
try:
    PATH = "Problem2\chromedriver.exe"
    URL = "https://www.theedgemarkets.com/article/gdex-stands-benefit-pickup-ecommerce-activities-says-kenanga-research"
    driver = webdriver.Chrome(PATH)
    savePath = 'Problem2\GDEX\Article 1'
    fileName1 = "sample.txt"
    fileName2 = "data.txt"
    sampleText = os.path.join(savePath, fileName1)
    dataText = os.path.join(savePath, fileName2)

    driver.get(URL)

    text_file = open(sampleText, "w")

    page = driver.page_source
    page_soup = BeautifulSoup(page, 'html.parser')

    article = page_soup.find('div', attrs={'class': 'article_content'})

    for p in article.find_all('p'):
        n = text_file.write(p.text + "\n")

    # 5(b)

    text_file = open(sampleText, "r")
    wordstring = text_file.read()
    wordstring = wordstring.lower()
    wordstring = wordstring.replace('"', "")
    wordlist = re.findall(r"[\w&']+", wordstring)
    #print(wordlist)
    
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

    # excludeStopw()
    # positive()
    # negative()
    # neutral()
    # calc()
    # posGraph()
    # negGraph()
    # PosNegGraph()
    # CountGraph()
    webscrapwrite2.article2()
    webscrapwrite3.article3()
    
except FileNotFoundError:
    print("file not found")
