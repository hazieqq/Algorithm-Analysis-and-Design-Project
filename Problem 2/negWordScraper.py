from selenium import webdriver
from bs4 import BeautifulSoup
import re


def webScrape(driver, URL, fileName):
    driver.get(URL)
    text_file = open(fileName, "w")
    page = driver.page_source
    page_soup = BeautifulSoup(page, 'html.parser')

    article = page_soup.find('div', attrs={'class': 'entry-content clear'})

    for p in article.find_all('p'):
        text_file.write(p.text)

    text_file.close()


def readNegativeFile(fileName):
    file = open(fileName, 'r')
    text = file.read()
    file.close()
    return text


def writeNegativeFile(text):
    text = re.sub("[(,){}<>:.[']", '', text)
    text = text.replace(",  ", '')
    text = re.sub("\s\s+", "\n", text)
    text = text.lower()
    File = open(r"negativeWord.txt", "w")
    File.write(text)
    File.close()


def readSampleText():
    filename1 = 'sample.txt'
    file1 = open(filename1, 'r')
    text = file1.read()
    text = text.lower()
    text = re.findall(r'[\w]+', text)
    file1.close()
    return text


def outputNegative(fileName1, fileName2):
    # compare two files, if same output put into another file
    # (txt file website yang kita scrape with scraped negative file)
    with open('update_news.txt', 'r') as file1:
        with open(fileName1, 'r') as file2:
            same = set(file1).intersection(file2)
    same.discard('\n')

    with open(fileName2, 'w') as file_out:
        for line in same:
            file_out.write(line)


def readOutputNegative(fileName2):
    file2 = open(fileName2, 'r')
    text = file2.read()
    text = text.split()
    file2.close()
    return text


def writeFreqNeg(text1, text2):
    index = 0
    sum = 0

    writeFile = open('freqNeg.txt', 'w')
    for i in range(len(text2)):
        for j in range(len(text1)):
            if text1[j] == text2[i]:
                index += 1
        print('{},{}'.format(text2[i], index))
        writeFile.write('{},{}'.format(text2[i], index)+"\n")
        sum += index
        index = 0

    writeFile.close()
    return sum


def writeTotalNeg(sum):
    with open('totalPosNeg.txt', 'a') as file:
        file.write('{},{}'.format('Negative Words', sum)+"\n")


try:
    PATH = "Problem 2\chromedriver.exe"
    URL = "https://positivewordsresearch.com/list-of-negative-words/"

    driver = webdriver.Chrome(PATH)
    fileName1 = 'negativeWord.txt'
    webScrape(driver, URL, fileName1)

    text = readNegativeFile(fileName1)
    writeNegativeFile(text)
    text1 = readSampleText()

    fileName2 = 'OutputNegative.txt'
    outputNegative(fileName1, fileName2)
    text2 = readOutputNegative(fileName2)
    sum = writeFreqNeg(text1, text2)
    writeTotalNeg(sum)

except FileNotFoundError:
    print("file not found")
