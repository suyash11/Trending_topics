"""Main module to aggregate all the modules."""

import sys
import constants
import csv_to_str
import stopwords
import nltk_stemmer


def main(csv_file=None, number_of_articles=None):
    """
    Main method.

    Purpose:
        Aggregator and a central controller to control all the modules
    Working:
        >> main(csv_file='~/suyash/Sample.csv')
    """
    working_string = csv_to_str.csv_2_str(csv_file=csv_file)
    stopword_set = stopwords.stopwords()
    print nltk_stemmer.word_tokenizer(string_to_tokenize=working_string,
                                      stopset=stopword_set,
                                      top_number_of_articles=number_of_articles)
if __name__ == '__main__':
    try:
        csv_file = sys.argv[1]
    except Exception as e:
        csv_file = constants.csv_file
    try:
        number_of_articles = sys.argv[2]
    except Exception as e:
        csv_file = constants.number_of_articles
    main(csv_file=csv_file,
         number_of_articles=number_of_articles)
