import cleaningTools
import pandas as pd
import numpy as np

# assumed location of big lyrics file
df_large = pd.read_csv('380000-lyrics-from-metrolyrics/lyrics.csv')
# prints unique genres in the dataframe
print(df_large.genre.unique())

df_small = pd.read_csv('lyrics_small.csv')
print(df_small)
print(list(df_small.columns.values))

# for index, row in df_small.iterrows():
#     lyrics = row['lyrics'].replace('\n', ' ')
#     cleaned_lyrics_list = cleaningTools.normalize(lyrics)

    # QUESTION: Do we want a single string or a list of strings in the dataframe?
    # TODO: assign lyrics list back into dataframe for later use

