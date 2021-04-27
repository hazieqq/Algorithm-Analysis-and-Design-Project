import re

try:
    stop_word_file = open("stopwords.txt", "r")

    article = open("sample.txt","r")

    articlestring = article.read()
    articlestring = articlestring.lower()
    articlelist = re.findall(r"[\w']+", articlestring)


    wordstring = stop_word_file.read()
    wordlist = wordstring.split()


    for i in range(len(articlelist)):
        # print(articlelist[i])
        for j in range(len(wordlist)):
            articlelist[i]=articlelist[i].translate(',."')
            if articlelist[i] == wordlist[j]:
                articlelist[i] = articlelist[i].replace(wordlist[j],"")

    while("" in articlelist):
        articlelist.remove("")
    print(articlelist)


    update_news=open("update_news.txt","w")


    for i in range(len(articlelist)):
        update_news.write(str(articlelist[i]))
        update_news.write("\n")



    stop_word_file.close()

except FileNotFoundError:
    print("file not found")