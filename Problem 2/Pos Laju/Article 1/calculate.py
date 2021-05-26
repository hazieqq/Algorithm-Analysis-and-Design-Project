import re
import os

def formula(x, y, z):
  score = (x-y)/z
  print('%s %.4f' % ('the score is: ', score))
  return score

def calcPos(text1, text2):
  index = 0
  sum = 0

  for i in range(len(text2)):
      for j in range(len(text1)):
          if text1[j] == text2[i]:
              index += 1

      sum += index
      index = 0

  return sum


def readSampleText(savePath):
    fileName1 = 'sample.txt'
    sampleText = os.path.join(savePath, fileName1)

    file1 = open(sampleText, 'r')
    text = file1.read()
    text = text.lower()
    text = re.findall(r'[\w]+', text)
    file1.close()
    return text



def calc():
  try:
    savePath = 'Problem 2\Pos Laju\Article 1'
    text1 = readSampleText(savePath)       #read sample text in list

    fileName1 = 'OutputPositive.txt'
    outPosText = os.path.join(savePath, fileName1)
    openPos = open(outPosText, 'r')
    wordstring1 = openPos.read()
    text2 = wordstring1.split()

    x = calcPos(text1, text2)

    fileName2 = 'OutputNegative.txt'
    outNegText = os.path.join(savePath, fileName2)
    openNeg = open(outNegText, 'r')
    wordstring2 = openNeg.read()
    text3 = wordstring2.split()

    y = calcPos(text1, text3)

    fileName3 = 'neutralWord.txt'
    outNEUText = os.path.join(savePath, fileName3)
    openNEU = open(outNEUText, 'r')
    wordstring3 = openNEU.read()
    text4 = wordstring3.split()

    z = calcPos(text1, text4)

    return formula(x, y, z)

  except FileNotFoundError:
    print("file not found")

