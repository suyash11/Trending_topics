#!/usr/bin/python
"""Main module to aggregate all the modules."""

import sys
import argparse
import stopwords
import constants
import csv_to_str
import nltk_stemmer


__author__ = 'Suyash Shukla'


def get_args():
    """The function parses and return arguments passed."""
    # Assign description to the help doc
    parser = argparse.ArgumentParser(
        description="""Script retrieves receives the csv file and
                       outputs the relevant news articles""")
    # Add arguments
    parser.add_argument(
        '-c', '--csv_file',
        help='CSV file path as a string', required=False,
        nargs='?', default=constants.csv_file,
        type=str)
    parser.add_argument(
        '-n', '--number_of_articles', type=int,
        help='Number of search results to be found', required=False,
        default=constants.number_of_articles)
    # Array for all arguments passed to script
    args = parser.parse_args()
    # Return all variable values
    return args.csv_file, args.number_of_articles


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
    csv_file, number_of_articles = get_args()
    main(csv_file=csv_file,
         number_of_articles=number_of_articles)
