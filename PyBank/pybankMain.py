# Import dependencies
import csv
import os

# Create filepath
dataSet = "PyBank/Resources/budget_data.csv"
path = os.path.join(dataSet)

with open(dataSet, 'r') as input_file:
    csvreader = csv.reader(input_file, delimiter=",")

    for row in csvreader:
        print(row)

# Build financial analysis function


