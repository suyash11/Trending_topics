"""NLTK-Stemmer module."""

import heapq
from collections import Counter
from nltk.tokenize import word_tokenize
from nltk.stem.snowball import EnglishStemmer

stemmer = EnglishStemmer()


def word_tokenizer(string_to_tokenize=None,
                   stopset=None,
                   top_number_of_articles=None):
    """
    word_tokenize method.

    Packages used:
        - heapq
        - collections
        - nltk

    Purpose:
        - tokenize words
        - stemm the words
        - count 'tf' of the words

    Execution:
        >> word_tokenize(string_to_tokenize='Sample query',
                         stopset=stopset,
                         top_number_of_articles=10)
        >> ['india', 'arts', .......]
    """
    tokens = word_tokenize(string_to_tokenize)
    tokens = [stemmer.stem(w) for w in tokens if w not in stopset]
    counts = Counter(tokens)
    return heapq.nlargest(int(top_number_of_articles), counts, key=counts.get)
