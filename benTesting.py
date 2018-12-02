# index, song, year, artist, genre, lyrics

import pandas as pd
import numpy as np

def header(desc):
    d = '[ {} ]'.format(desc)
    print('-'*len(d))
    print(d)
    print('-'*len(d))

df = pd.read_csv('lyrics_small.csv')

#replace carriage returns
header('replaced carriage returns')
df = df.replace({'\n': ' '}, regex=True)

#count the words in each song
df['word_count'] = df['lyrics'].str.split().str.len()

#let's see what the songs with 1 word look like
df1 = df.loc[df['word_count'] == 1]

#elimintate the 1-word songs and review the data again
df = df[df['word_count'] != 1]
df['word_count'].groupby(df['genre']).describe()


print(df)