from io import IncrementalNewlineDecoder
from selenium import webdriver
from bs4 import BeautifulSoup
from collections import Counter
import re
import os
from Citylink.Article1.PosLajuArticle1.Article3 import swprogram,posWordScraper,negWordScraper,neutralWord,calculate,posWordGraph,negWordGraph,posNegWordGraph,wordCountGraph


def article3():

#5 (a)
    try:
        PATH = "Problem 2\chromedriver.exe"
        URL = "https://www.freemalaysiatoday.com/category/nation/2021/02/22/pos-malaysia-probes-video-of-of-postman-shooting-a-dog/"
        driver = webdriver.Chrome(PATH)
        savePath = 'Problem 2\Citylink\Article1\PosLajuArticle1\Article3'
        fileName1 = "sample.txt"
        fileName2 = "data.txt"
        sampleText = os.path.join(savePath, fileName1)
        dataText = os.path.join(savePath, fileName2)

        driver.get(URL)

        text_file = open(sampleText, "w", encoding="cp437", errors='ignore')

        page = driver.page_source
        page_soup = BeautifulSoup(page, 'html.parser')
        
        article = page_soup.find('div', attrs={'class': 'td-post-content tagdiv-type'})

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
        # wordCountGraph.CountGraph()
        return x

    except FileNotFoundError:
        print("file not found")
