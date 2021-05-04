import pandas as pd
import plotly.express as px


def textToCSV(textFile, csvFile):
    df = pd.read_csv(textFile, header=None)
    df.columns = ['Positive Words', 'Frequency']
    df.to_csv(csvFile, index=None)


def createGraph(csvFile):
    df = pd.read_csv(csvFile)
    fig = px.bar(df, y='Frequency', x='Positive Words')
    fig.update_traces(texttemplate='', textposition='outside')
    fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
    fig.show()


textFile = 'freqPos.txt'
csvFile = 'freqPos.csv'
textToCSV(textFile, csvFile)
createGraph(csvFile)
