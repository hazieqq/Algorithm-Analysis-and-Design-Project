import pandas as pd
import plotly.express as px
import os


def textToCSV(textFile, csvFile):
    df = pd.read_csv(textFile, header=None)
    df.columns = ['Negative Words', 'Frequency']
    df.to_csv(csvFile, index=None)


def createGraph(csvFile):
    df = pd.read_csv(csvFile)
    fig = px.bar(df, y='Frequency', x='Negative Words')
    fig.update_traces(texttemplate='', textposition='outside')
    fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
    fig.show()

#run
def negGraph():
    savePath = 'Problem 2\Citylink\Article1\DHLArticle1\Article2'
    fileName1 = 'freqNeg.txt'
    fileName2 = 'freqNeg.csv'
    textFile = os.path.join(savePath, fileName1)
    csvFile = os.path.join(savePath, fileName2)
    textToCSV(textFile, csvFile)
    createGraph(csvFile)

