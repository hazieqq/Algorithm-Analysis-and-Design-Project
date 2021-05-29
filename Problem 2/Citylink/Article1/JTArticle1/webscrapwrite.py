from io import IncrementalNewlineDecoder
from selenium import webdriver
from bs4 import BeautifulSoup
from collections import Counter
import re
import os
# from swprogram import excludeStopw
# from posWordScraper import positive
# from negWordScraper import negative
# from neutralWord import neutral
# from calculate import calc
# from posWordGraph import posGraph
# from negWordGraph import negGraph
# from posNegWordGraph import PosNegGraph
# from wordCountGraph import CountGraph


# from Article2 import webscrapwrite2
# from Article3 import webscrapwrite3

from Citylink.Article1.JTArticle1 import swprogram,posWordScraper,negWordScraper,neutralWord,calculate,posWordGraph,negWordGraph,posNegWordGraph,wordCountGraph
from Citylink.Article1.JTArticle1.Article3 import webscrapwrite3
from Citylink.Article1.JTArticle1.Article2 import webscrapwrite2


def JT():

    #5 (a)
    try:
        PATH = "Problem 2\chromedriver.exe"
        URL = "https://www.nst.com.my/news/nation/2021/02/663907/violent-sorting-parcels-jt-apologises-customers"
        driver = webdriver.Chrome(PATH)
        savePath = 'Problem 2\Citylink\Article1\JTArticle1'
        fileName1 = "sample.txt"
        fileName2 = "data.txt"
        sampleText = os.path.join(savePath, fileName1)
        dataText = os.path.join(savePath, fileName2)

        driver.get(URL)

        text_file = open(sampleText, "w")

        page = driver.page_source
        page_soup = BeautifulSoup(page, 'html.parser')

        article = page_soup.find('div', attrs={'class': 'field field-body'})

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

        y = webscrapwrite2.article2()
        z = webscrapwrite3.article3()

        total = x + y + z
        return total

    except FileNotFoundError:
        print("file not found")
