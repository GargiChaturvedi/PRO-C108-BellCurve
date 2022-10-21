import pandas
import csv
import plotly.figure_factory as ff

df = pandas.read_csv('data.csv')
means = df.groupby('Mobile Brand')['Avg Rating'].mean()
print(means)

fig = ff.create_distplot([means.tolist()], ['Brands'], show_hist=False, colors=['deeppink'])
fig.show()