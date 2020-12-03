# Imports needed classes
import csv
from sys import argv, exit
from cs50 import SQL


def main():
    # Checks correct usage
    if len(argv) != 2:
        print("Usage: python import.py data.csv")
        exit(1)

    # Gets data from opened database
    db = SQL("sqlite:///students.db")
    data = db.execute(f"SELECT first, middle, last, birth FROM students WHERE house == \"{argv[1]}\" ORDER BY last, first;")

    # prints each student's info in correct format
    for person in data:
        if person["middle"] == None:
            print(person["first"], person["last"] + ", born", person["birth"])
        else:
            print(person["first"], person["middle"], person["last"] + ", born", person["birth"])


main()