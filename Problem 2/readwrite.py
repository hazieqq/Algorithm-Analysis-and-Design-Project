from selenium import webdriver
from bs4 import BeautifulSoup, NavigableString
from collections import Counter

#5 (a)
try:
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)

    driver.get("https://www.nst.com.my/news/nation/2021/02/663907/violent-sorting-parcels-jt-apologises-customers")

    text_file = open("sample.txt", "w")
    # n = text_file.write('haha to pythonexamples.org')
    # text_file.close()

    page = driver.page_source
    page_soup = BeautifulSoup(page,'html.parser')

    article = page_soup.find('div',attrs={'class':'field field-body'}) 
    # print(article.text)

    for p in article.find_all('p'):
        n = text_file.write(p.text + "\n")

    #5(b)

    text_file = open("sample.txt", "r")
    wordstring = text_file.read()
    wordstring = wordstring.lower()
    wordstring = wordstring.replace('"',"")
    wordlist = wordstring.split()

    #remove duplicate

    c = Counter(wordlist)

    wordfreq = []
    for w in c.keys():
        s = str(c.keys())
        wordfreq.append(s.count(w))

    print("Pairs\n" + str(list(zip(c.keys(), wordfreq))))

    text_file.close()

except FileNotFoundError:
    print("file not found")
