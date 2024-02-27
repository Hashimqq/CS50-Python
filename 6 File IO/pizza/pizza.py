import csv
from tabulate import *
import sys


def main():
    check()
    try:
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            print(tabulate(reader, headers='keys', tablefmt='grid'))

    except FileNotFoundError:
        sys.exit("File not found")


def check():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if ".csv" not in sys.argv[1]:
        sys.exit("Not a CSV file")


if __name__ == '__main__':
    main()
