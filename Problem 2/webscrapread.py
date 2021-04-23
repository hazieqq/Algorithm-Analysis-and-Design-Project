
text_file = open("sample.txt", "r")

wordstring = text_file.read()
wordlist = wordstring.split()

wordfreq = []
for w in wordlist:
    wordfreq.append(wordlist.count(w))

print("Pairs\n" + str(list(zip(wordlist, wordfreq))))

text_file.close()