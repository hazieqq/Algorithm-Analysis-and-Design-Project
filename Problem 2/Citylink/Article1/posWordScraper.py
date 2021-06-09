from selenium import webdriver
from bs4 import BeautifulSoup
import re
import os


def webScrape(driver, URL, fileName):
    driver.get(URL)
    text_file = open(fileName, "w")
    page = driver.page_source
    page_soup = BeautifulSoup(page, 'html.parser')

    article = page_soup.find('div', attrs={'class': 'entry-content clear'})

    for p in article.find_all('p'):
        text_file.write(p.text)

    text_file.close()


def readPositiveFile(fileName):
    file = open(fileName, 'r')
    text = file.read()
    file.close()
    return text


def writePositiveFile(text, fileName):
    text = re.sub("[(,){}<>:.[']", '', text)
    text = text.replace(",  ", '')
    text = re.sub("\s\s+", "\n", text)
    text = text.lower()
    File = open(fileName, "w")
    File.write(text)
    File.close()


def readSampleText(savePath):
    fileName1 = 'sample.txt'
    sampleText = os.path.join(savePath, fileName1)

    file1 = open(sampleText, 'r')
    text = file1.read()
    text = text.lower()
    text = re.findall(r'[\w]+', text)
    file1.close()
    return text

def search(pat, txt):
    M = len(pat)
    N = len(txt)

    for i in range(N - M + 1):
        j = 0
            
        while(j < M):                          #size of pattern
            if (txt[i + j] != pat[j]):
                break
            j += 1

        if (j == M and M == N):
            return True



def outputPositive(fileName1, fileName2, savePath):
    # compare two files, if same output put into another file
    # (txt file website yang kita scrape with scraped positive file)
    fileName = 'update_news.txt'
    upNewsText = os.path.join(savePath, fileName)
    filesatu = open(fileName1,'r')
    filedua = open(upNewsText,'r')
    textsatu = filesatu.read()
    textdua = filedua.read()
    textsatu = textsatu.splitlines()
    textdua = textdua.split()
    pos =[]
    for i in range(len(textsatu)):
        for j in range(len(textdua)):
            if search(textsatu[i],textdua[j]):
                pos.append(textdua[j])
            


    # with open(upNewsText, 'r') as file1:
    #     with open(fileName1, 'r') as file2:
    #         same = set(file1).intersection(file2)
    # print(same)
    # same.discard('\n')

    with open(fileName2, 'w') as file_out:
        for i in range(len(pos)):
            file_out.write(pos[i])
            file_out.write('\n')
        # for line in same:
        #     file_out.write(line)


def readOutputPositive(fileName2):
    file2 = open(fileName2, 'r')
    text = file2.read()
    text = text.split()
    file2.close()
    return text


def writeFreqPos(text1, text2, savePath):
    index = 0
    sum = 0
    fileName = 'freqPos.txt'
    freqPosText = os.path.join(savePath, fileName)

    writeFile = open(freqPosText, 'w')
    for i in range(len(text2)):
        for j in range(len(text1)):
            if text1[j] == text2[i]:
                index += 1
        #print('{},{}'.format(text2[i], index))
        writeFile.write('{},{}'.format(text2[i], index)+"\n")
        sum += index
        index = 0

    writeFile.close()
    return sum


def writeTotalPos(sum, savePath):
    fileName = 'totalPosNeg.txt'
    totalPosNegText = os.path.join(savePath, fileName)

    with open(totalPosNegText, 'w') as file:
        file.write('{},{}'.format('Positive Words', sum)+"\n")

def positive():
    try:
        # PATH = "Problem 2\chromedriver.exe"
        # URL = "http://positivewordsresearch.com/list-of-positive-words/"
        # driver = webdriver.Chrome(PATH)

        savePath = 'Problem 2\Citylink\Article1'
        fileName1 = 'positiveWord.txt'
        posWordText = os.path.join(savePath, fileName1)
        # webScrape(driver, URL, posWordText)

        # text = readPositiveFile(posWordText) #read postive word
        # writePositiveFile(text, posWordText) #clean positive file
        text1 = readSampleText(savePath)       #read sample text in list

        fileName2 = 'OutputPositive.txt'
        outPosText = os.path.join(savePath, fileName2)
        outputPositive(posWordText, outPosText, savePath)
        text2 = readOutputPositive(outPosText) #positive word that are in sample in list
        sum = writeFreqPos(text1, text2, savePath)
        writeTotalPos(sum, savePath)
        
        # driver.close()

    except FileNotFoundError:
        print("file not found")

