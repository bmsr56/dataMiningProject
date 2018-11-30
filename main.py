import cleaningTools
import pandas as pd
import numpy as np
import string

df_small = pd.read_csv('lyrics_small.csv')

print(df_small)
print(list(df_small.columns.values))

for index, row in df_small.iterrows():
    print(row['song'], row['genre'])
    print(type(row['lyrics']))
    stringA = row['lyrics'].replace('\n', ' ')
    print(type(stringA))

    print(cleaningTools.normalize(stringA))
