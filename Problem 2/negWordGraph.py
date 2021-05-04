import pandas as pd
import plotly.express as px


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


textFile = 'freqNeg.txt'
csvFile = 'freqNeg.csv'
textToCSV(textFile, csvFile)
createGraph(csvFile)
