import re
import os

try:
    stop_word_file = open("Problem 2\stopwords.txt", "r")
    savePath = 'Problem 2\DHL\Article 1'
    fileName1 = "sample.txt"
    fileName2 = "update_news.txt"
    sampleText = os.path.join(savePath, fileName1)
    updateNewsText = os.path.join(savePath, fileName2)

    article = open(sampleText, "r")
    articlestring = article.read()
    articlestring = articlestring.lower()
    articlelist = re.findall(r"[\w']+", articlestring)

    wordstring = stop_word_file.read()
    wordlist = wordstring.split()

    set1 = set(articlelist)
    set2 = set(wordlist)

    set1.difference_update(set2)

    articlelist1 = list(set1)

    # for i in range(len(articlelist)):
    #     print(articlelist[i])
    # for j in range(len(wordlist)):
    #     if re.search(articlelist[i],wordlist[j]):
    #         articlelist[i] = articlelist[i].replace(wordlist[j],"")
    #         if articlelist[i] == wordlist[j]:
    #             articlelist[i] = articlelist[i].replace(wordlist[j],"")

    # while("" in articlelist):
    #     articlelist.remove("")
    # print(articlelist)

    update_news = open(updateNewsText, "w")

    for i in range(len(articlelist1)):
        update_news.write(str(articlelist1[i]))
        update_news.write("\n")

    stop_word_file.close()

except FileNotFoundError:
    print("file not found")
