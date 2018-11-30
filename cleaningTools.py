import re
import string
import unicodedata
#   $ sudo pip3 install -U nltk
import nltk
#   $ pip3 install contractions
import contractions
#   $ pip3 install inflect
import inflect
from nltk import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import string

# replace contractions
def fix_contractions(str):
    return contractions.fix(str)

# removes non-ASCII characters from list
def remove_non_ascii(strA):
    return unicodedata.normalize('NFKD', strA).encode('ascii', 'ignore').decode('utf-8', 'ignore')

# make everything lowercase
def make_lowercase(strA):
    return strA.lower()

# removes punctuation
def remove_punctuation(lst):
    translator = lst.maketrans('', '', string.punctuation)
    return lst.translate(translator)

# replaces digits with text equivalent
def replace_numbers(input):
    # split input(string) into a list. str.isdigit() only checks if whole string is a digit not part,
    #   so can't run whole string though it.
    lst = input.split(' ')

    inflecter = inflect.engine()
    words = []
    for word in lst:
        # if it is an integer convert it to a string
        temp = word
        if temp.isdigit():
            temp = inflecter.number_to_words(word)
        words.append(temp)

    # the next function in the 'normalize' lineup needs a list so keep this a list
    return words

def remove_stopwords(lst):
# needs a list
    words = []
    for word in lst:
        if word not in stopwords.words('english'):
            words.append(word)
    return words


def lemmatize_words(lst):
# needs a list
    lemmatizer = WordNetLemmatizer()
    lemmas = []
    for word in lst:
        lemma = lemmatizer.lemmatize(word, pos='v')
        lemmas.append(lemma)
    return lemmas

def normalize(strA):
    strA = fix_contractions(strA)
    strA = remove_non_ascii(strA)
    strA = make_lowercase(strA)
    strA = remove_punctuation(strA)
    listA = replace_numbers(strA)
    listA = remove_stopwords(listA)
    listA = lemmatize_words(listA)
    return listA
