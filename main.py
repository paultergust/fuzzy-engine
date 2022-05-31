import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime as dt

def by_a_million(num):
    return num / 1_000_000

#read and setup dataframe from csv file
df = pd.read_csv('db.csv')
df = df.sort_values(by=['Date'])

#swap 'Budget' and 'Gross_Worldwide' in each list compreension to get different values

#set enum and mean by female protagonists
f_values = df.loc[df['Gender'] == 'Female']
f_values = [by_a_million(x) for x in f_values.Budget]
f_values = np.mean(f_values)

#set enum and mean by male protagonists
m_values = df.loc[df['Gender'] == 'Male']
m_values = [by_a_million(y) for y in m_values.Budget]
m_values = np.mean(m_values)

#set enum and mean by group protagonists
g_values = df.loc[df['Gender'] == 'Group']
g_values = [by_a_million(g) for g in g_values.Budget]
g_values = np.mean(g_values)

#label and group data
names = ['F', 'M', 'G']
values = [f_values, m_values, g_values]

plt.bar(names, values)
#plt.suptitle('subtitle')

#plt.show()
plt.savefig('image.png')

