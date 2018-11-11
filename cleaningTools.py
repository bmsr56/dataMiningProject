import re
import string
import unicodedata
#   $ sudo apt install python3-contractions
import nltk
#   $ pip3 install contractions
import contractions
#   $ pip3 install inflect
import inflect
from nltk import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


# replace contractions
def fix_contractions(lst):
    return contractions.fix(lst)

# removes non-ASCII characters from list
def remove_non_ascii(lst):
    words = []
    for word in lst:
        cleaning = unicodedata.normalize('NFKD', word).encode('ascii', 'ignore').decode('utf-8', 'ignore')
        words.append(cleaning)
    return words

# make everything lowercase
def make_lowercase(lst):
    words = []
    for word in lst:
        words.append(word.lowercase())
    return words

# removes punctuation
def remove_punctuation(lst):
    words = []
    for word in lst:
        temp = word.translate(None, ',!.;?')
        if temp != '':
            words.append(word)
    return words

def replace_numbers(lst):
    inflecter = inflect.engine()
    words = []
    for word in lst:
        # if it is an integer convert it to a string
        if word.isdigit():
            temp = inflecter.number_to_words(word)
        words.append(temp)
    return words

def remove_stopwords(lst):
    words = []
    for word in lst:
        if word not in stopwords.words('english'):
            words.append(word)
    return words

def lemmatize_words(lst):
    lemmatizer = WordNetLemmatizer()
    lemmas = []
    for word in lst:
        lemma = lemmatizer.lemmatize(word, pos='v')
        lemmas.append(lemma)
    return lemmas

def normalize(lst):
    lst = remove_non_ascii(lst)
    lst = make_lowercase(lst)
    lst = remove_punctuation(lst)
    lst = replace_numbers(lst)
    lst = remove_stopwords(lst)
    lst = lemmatize_words(lst)
    return lst
