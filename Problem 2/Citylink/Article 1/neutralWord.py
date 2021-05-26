import re
import os

def writeFreqNeg(text1, text2, savePath):
    index = 0
    sum = 0

    fileName = 'freqNeg.txt'
    freqNegText = os.path.join(savePath, fileName)

    writeFile = open(freqNegText, 'w')
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

def neutral():
    try:
        savePath = 'Problem 2\Citylink\Article 1'
        fileName = "update_news.txt"
        fileName1 = "positiveWord.txt"
        fileName2 = "negativeWord.txt"
        fileName3 = "neutralWord.txt"
        
        positive = os.path.join(savePath, fileName1)
        negative = os.path.join(savePath, fileName2)
        updateNews = os.path.join(savePath, fileName)
        neutralWord = os.path.join(savePath, fileName3)

        article = open(updateNews, "r")
        articlestring = article.read()
        articlestring = articlestring.lower()
        articlelist = re.findall(r"[\w']+", articlestring)

        positive_word_file = open(positive, "r")
        wordstring1 = positive_word_file.read()
        poslist = wordstring1.split()

        negative_word_file = open(negative, "r")
        wordstring2 = negative_word_file.read()
        neglist = wordstring2.split()

        set1 = set(articlelist)
        set2 = set(poslist)
        set3 = set(neglist)

        set1.difference_update(set2)

        set1.difference_update(set3)

        articlelist1 = list(set1)
        
        neutral_word = open(neutralWord, "w")

        for i in range(len(articlelist1)):
            neutral_word.write(str(articlelist1[i]))
            neutral_word.write("\n")

        neutral_word.close()


    except FileNotFoundError:
        print("file not found")

