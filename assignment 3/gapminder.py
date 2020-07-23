#import necessary modules
import pandas as pd
import numpy as np
import seaborn as sns #need to install no default install

#read the data using pandas
df = pd.read_csv('gapminder-FiveYearData.csv')

#pivot_table = df.pivot_table(values='lifeExp', index='continent', columns='year')

#making pivot by hands dirty using groupby
pivot = df.groupby(['continent', 'year'])['lifeExp'].aggregate('mean').unstack()
#plot the pivot dataframe to seaborn 
sns_plot= sns.heatmap(pivot)
#output the figure into png file
sns_plot.figure.savefig("output.png")
