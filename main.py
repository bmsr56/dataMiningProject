import cleaningTools
import pandas as pd
import numpy as np

df_small = pd.read_csv('lyrics_small.csv')

print(df_small)
print(list(df_small.columns.values))

for index, row in df_small.iterrows():
    lyrics = row['lyrics'].replace('\n', ' ')
    cleaned_lyrics_list = cleaningTools.normalize(lyrics)

    # TODO: assign lyrics list back into dataframe for later use
