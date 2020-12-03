# Imports needed classes
import csv
from sys import argv, exit
from cs50 import SQL


def main():
    # Checks correct usage
    if len(argv) != 2:
        print("Usage: python import.py data.csv")
        exit(1)

    # Opens the csv and the database
    db = SQL("sqlite:///students.db")

    with open(argv[1], "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            # Insert the names
            names = row["name"].split(" ")
            first = names[0]
            middle = None
            last = names[len(names) - 1]

            if len(names) == 3:
                middle = names[1]

            db.execute("INSERT INTO students (first, middle, last, house, birth) VALUES(?, ?, ?, ?, ?)",
                       first, middle, last, row["house"], int(row["birth"]))


main()