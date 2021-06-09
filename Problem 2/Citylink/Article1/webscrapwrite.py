from io import IncrementalNewlineDecoder
from selenium import webdriver
from bs4 import BeautifulSoup
from collections import Counter
import re
import os
from Citylink.Article1.swprogram import excludeStopw
from Citylink.Article1.posWordScraper import positive
from Citylink.Article1.negWordScraper import negative
from Citylink.Article1.neutralWord import neutral
from Citylink.Article1.calculate import calc
from Citylink.Article1.posWordGraph import posGraph
from Citylink.Article1.negWordGraph import negGraph
from Citylink.Article1.posNegWordGraph import PosNegGraph
from Citylink.Article1.wordCountGraph import CountGraph

from Citylink.Article1.Article2 import webscrapwrite2
from Citylink.Article1.Article3 import webscrapwrite3
# import sys

# sys.path.append("..")

from Citylink.Article1.DHLArticle1.webscrapwrite1 import dhl
from Citylink.Article1.GDEXArticle1.webscrapwrite import GDEX
from Citylink.Article1.JTArticle1.webscrapwrite import JT
from Citylink.Article1.JTArticle1.webscrapwrite import JT
from Citylink.Article1.PosLajuArticle1.webscrapwrite import PosLaju


def City():

    #5 (a)
    try:
        PATH = "Problem 2\chromedriver.exe"
        URL = "https://themalaysianreserve.com/2017/03/31/city-link-targets-20-revenue-growth-with-new-super-hub/"
        driver = webdriver.Chrome(PATH)
        savePath = 'Problem 2\Citylink\Article1'
        fileName1 = "sample.txt"
        fileName2 = "data.txt"
        sampleText = os.path.join(savePath, fileName1)
        dataText = os.path.join(savePath, fileName2)

        driver.get(URL)

        text_file = open(sampleText, "w")

        page = driver.page_source
        page_soup = BeautifulSoup(page, 'html.parser')

        article = page_soup.find(
            'section', attrs={'class': 'single-post-content clearfix'})

        for p in article.find_all('p'):
            n = text_file.write(p.text + "\n")

        # 5(b)

        text_file = open(sampleText, "r")
        wordstring = text_file.read()
        wordstring = wordstring.lower()
        wordstring = wordstring.replace('"', "")
        wordlist = re.findall(r"[\w&']+", wordstring)
        # print(wordlist)

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
        neutral()
        x = calc()
        # posGraph()
        # negGraph()
        # PosNegGraph()
        # CountGraph()

        y = webscrapwrite2.article2()
        z = webscrapwrite3.article3()

        print(x)
        print(y)
        print(z)

        totalCity = x + y + z
        totalDhl = dhl()
        totalGDEX = GDEX()
        totalJT = JT()
        totalPosLaju = PosLaju()

        # arr = [totalCity, totalDhl, totalGDEX, totalJT, totalPosLaju]
        arr = {'City-Link': totalCity, 'DHL': totalDhl, 'GDEX': totalGDEX,
               'J&T': totalJT, 'PosLaju': totalPosLaju}

        print("City-Link:", totalCity)
        print("DHL:", totalDhl)
        print("GDEX:", totalGDEX)
        print("J&T:", totalJT)
        print("PosLaju:", totalPosLaju)
        print()

        return arr
        return 0
    except FileNotFoundError:
        print("file not found")
