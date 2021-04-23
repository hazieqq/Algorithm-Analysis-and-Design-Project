
stop_word_file = open("stopwords.txt", "r")

wordstring = stop_word_file.read()
wordlist = wordstring.split()

print("Stopword: " + str(list(wordlist))) 



stop_word_file.close()