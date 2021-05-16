from io import IncrementalNewlineDecoder
from selenium import webdriver
from bs4 import BeautifulSoup
from collections import Counter
import re
import os
# from swprogram import excludeStopw
# from posWordScraper import positive
# from negWordScraper import negative
# from posWordGraph import posGraph
# from negWordGraph import negGraph
# from posNegWordGraph import PosNegGraph
# from wordCountGraph import CountGraph
from swprogram import *
from posWordScraper import *
from negWordScraper import *
from posWordGraph import *
from negWordGraph import *
from posNegWordGraph import *
from wordCountGraph import *

#5 (a)
try:
    PATH = "Problem 2\chromedriver.exe"
    URL = "https://www.thestar.com.my/business/business-news/2021/04/30/post-malaysia-to-carry-on-strong-momentum-seen-in-3q-fy20"
    driver = webdriver.Chrome(PATH)
    savePath = 'Problem 2\Pos Laju\Article 1'
    fileName1 = "sample.txt"
    fileName2 = "data.txt"
    sampleText = os.path.join(savePath, fileName1)
    dataText = os.path.join(savePath, fileName2)

    driver.get(URL)

    text_file = open(sampleText, "w", encoding="cp437", errors='ignore')

    page = driver.page_source
    page_soup = BeautifulSoup(page, 'html.parser')
    
    article = page_soup.find('div', attrs={'id': 'story-body'})

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

    excludeStopw()
    positive()
    negative()
    posGraph()
    negGraph()
    PosNegGraph()
    CountGraph()

except FileNotFoundError:
    print("file not found")
