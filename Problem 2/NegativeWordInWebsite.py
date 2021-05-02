from selenium import webdriver
from bs4 import BeautifulSoup, NavigableString
from collections import Counter
import re
import string

try:
    PATH = "Problem 2\chromedriver.exe"
    driver = webdriver.Chrome(PATH)

    driver.get("https://positivewordsresearch.com/list-of-negative-words/")

    text_file = open("negativeWord.txt", "w")
    page = driver.page_source
    page_soup = BeautifulSoup(page,'html.parser')

    article = page_soup.find('div',attrs={'class':'entry-content clear'}) 

    for p in article.find_all('p'):
        n = text_file.write(p.text)

    text_file.close()

    filename = 'negativeWord.txt'
    file = open(filename, 'r')
    text = file.read()
    file.close()

    text = re.sub("[(,){}<>:.[']", '', text)
    text = text.replace(",  ", '')
    text = re.sub("\s\s+" , "\n", text)
    text = text.lower()
    print(text)
    File = open(r"negativeWord.txt", "w")
    File.write(text)
    File.close()

    #compare two files, if same output put into another file 
    #(txt file website yang kita scrape with scraped positive file)
    with open('update_news.txt', 'r') as file1:
        with open('negativeWord.txt', 'r') as file2:
            same = set(file1).intersection(file2)

    same.discard('\n')

    with open('OutputNegative.txt', 'w') as file_out:
        for line in same:
            file_out.write(line)

except FileNotFoundError:
    print("file not found")