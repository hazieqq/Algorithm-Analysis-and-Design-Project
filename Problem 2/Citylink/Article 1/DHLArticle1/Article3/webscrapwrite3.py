from io import IncrementalNewlineDecoder
from selenium import webdriver
from bs4 import BeautifulSoup
from collections import Counter
import re
import os

from DHLArticle1.Article3 import swprogram,posWordScraper,negWordScraper,neutralWord,calculate,posWordGraph,negWordGraph,posNegWordGraph,wordCountGraph
#5 (a)

def article3():

    try:
        PATH = "Problem 2\chromedriver.exe"
        URL = "https://www.taiwannews.com.tw/en/news/4073412"
        driver = webdriver.Chrome(PATH)
        savePath = 'Problem 2\Citylink\Article 1\DHLArticle1\Article3'
        fileName1 = "sample.txt"
        fileName2 = "data.txt"
        sampleText = os.path.join(savePath, fileName1)
        dataText = os.path.join(savePath, fileName2)

        driver.get(URL)

        text_file = open(sampleText, "w")

        page = driver.page_source
        page_soup = BeautifulSoup(page, 'html.parser')

        article = page_soup.find('article', attrs={'class': 'container-fluid article'})

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

        swprogram.excludeStopw()
        posWordScraper.positive()
        negWordScraper.negative()
        neutralWord.neutral()
        x = calculate.calc()
        # posWordGraph.posGraph()
        # negWordGraph.negGraph()
        # posNegWordGraph.PosNegGraph()
        wordCountGraph.CountGraph()
        return x

    except FileNotFoundError:
        print("file not found")
