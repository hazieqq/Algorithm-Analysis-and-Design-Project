import pandas as pd
import plotly.express as px
import dash

df = pd.read_csv('data.txt')
df.columns = ['Words','Frequency']
df.to_csv('data.csv', index=False)
df = pd.read_csv('data.csv')
fig = px.bar(df, y='Frequency', x='Words')
fig.update_traces(texttemplate='', textposition='outside')
fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
fig.show()
