# Import the os module and the module for reading CSV files
import os
import csv

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

# Generating output
file_to_output = "PyBank Analysis Summary"

#Create lists
delta_months = []
delta_revenue = []

#Starting points for future math
months_total = 0
previous_revenue = 0
revenue_total = 0

#Tracking Greatests
increase_greatest = ["", 0]
decrease_greatest = ["", 99999999999999]

# Read the csv and convert it into a dictionary using DictReader
with open(csvpath) as financial_data:
    reader = csv.DictReader(financial_data)


    for row in reader:

        #Totals Tracking
        months_total = months_total + 1
        revenue_total = revenue_total + int(row["Profits/Losses"])

        #Revenue Delta Tracking
        revenue_delta = int(row["Profits/Losses"]) - previous_revenue
        previous_revenue = int(row["Profits/Losses"])
        delta_revenue = delta_revenue + [previous_revenue]
        delta_months = delta_months + [row["Date"]]

