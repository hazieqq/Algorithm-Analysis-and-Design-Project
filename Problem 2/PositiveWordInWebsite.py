from selenium import webdriver
from bs4 import BeautifulSoup, NavigableString
from collections import Counter
import re
import string

try:
    PATH = "Problem 2\chromedriver.exe"
    driver = webdriver.Chrome(PATH)

    driver.get("http://positivewordsresearch.com/list-of-positive-words/")

    text_file = open("positiveWord.txt", "w")
    page = driver.page_source
    page_soup = BeautifulSoup(page,'html.parser')

    article = page_soup.find('div',attrs={'class':'entry-content clear'}) 

    for p in article.find_all('p'):
        n = text_file.write(p.text)

    text_file.close()

    filename = 'positiveWord.txt'
    file = open(filename, 'r')
    text = file.read()
    file.close()

    

    

    text = re.sub("[(,){}<>:.[']", '', text)
    text = text.replace(",  ", '')
    text = re.sub("\s\s+" , "\n", text)
    text = text.lower()
    File = open(r"positiveWord.txt", "w")
    File.write(text)

    File.close()

    filename1 = 'sample.txt'
    file1 = open(filename1,'r')
    text1 = file1.read()
    text1 = text1.lower()
    text1 = re.findall(r'[\w]+',text1)

    

    #compare two files, if same output put into another file 
    #(txt file website yang kita scrape with scraped positive file)
    with open('update_news.txt', 'r') as file1:
        with open('positiveWord.txt', 'r') as file2:
            same = set(file1).intersection(file2)

    same.discard('\n')

    with open('OutputPositive.txt', 'w') as file_out:
        for line in same:
            file_out.write(line)

    filename2 = 'OutputPositive.txt'
    file2 = open(filename2,'r')
    text2 = file2.read()
    text2 = text2.split()
    index =0

    for i in range(len(text2)):
        for j in range(len(text1)):
            if text1[j] == text2[i]:
                index += 1
        print('{},{}'.format(text2[i],index))
        index =0
except FileNotFoundError:
    print("file not found")