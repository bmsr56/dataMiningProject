import cleaningTools
import pandas as pd
import numpy as np
import plotly
import plotly.graph_objs as go


# assumed location of big lyrics file
df_large = pd.read_csv('380000-lyrics-from-metrolyrics/lyrics.csv')
# prints unique genres in the dataframe
# print(df_large.genre.unique())

df_small = pd.read_csv('lyrics_small.csv')
# print(df_small)
# print(list(df_small.song))

# for index, row in df_small.iterrows():
#     lyrics = row['lyrics'].replace('\n', ' ')
#     cleaned_lyrics_list = cleaningTools.normalize(lyrics)

    # QUESTION: Do we want a single string or a list of strings in the dataframe?
    # TODO: assign lyrics list back into dataframe for later use


print(pd.value_counts(df_large.genre).keys().tolist())  # .plot(kind="bar")
print(pd.value_counts(df_large.genre).tolist())         # .plot(kind="bar")


data = [
    go.Scatter(
        # assign x as the dataframe column 'x'
        x=pd.value_counts(df_large.genre).keys().tolist(),
        y=pd.value_counts(df_large.genre).tolist()
    )
]

plotly.offline.plot(data)
