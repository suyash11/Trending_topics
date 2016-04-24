"""CSV to string module."""
import csv


def csv_2_str(csv_file=None):
    """
    csv_2_str method.

    Packages used:
        csv

    Method:
        >> csv_2_str(csv_file='~/suyash/Sample.csv')
        returns a complete string with all headings(index=4)
        >> csv_2_str()
        picks csv_file from the constants file
    :return_string: The return string
    :f: file object
    :reader: reader object
    :row: iterator
    """
    return_string = str()
    f = open(csv_file, 'rt')
    try:
        reader = csv.reader(f)
        for row in reader:
            return_string += row[4]
    finally:
        f.close()
    return return_string
