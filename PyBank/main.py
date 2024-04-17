# Import the os module and the module for reading CSV files
import os
import csv

csvpath = os.path.join('.', 'Resources', 'budget_data.csv')

#Define the field names for two columns
fieldnames = ['Date', 'Profit/Losses']

#Create lists
delta_months = []
pandl_change_list = []

#Starting points for future math
months_total = 0
previous_pandl = 0
pandl_total = 0

# Read the csv and convert it into a dictionary using DictReader
with open(csvpath) as financial_data:
    reader = csv.DictReader(financial_data, fieldnames=fieldnames)
    next(reader)  # Skip the header row
    for row in reader:

        #Change in Months calculation
        months_total += 1
        delta_months.append(row["Date"])
        
        #Total Profits/Losses calculation
        pandl_total = pandl_total + int(row["Profit/Losses"])

        #Calculate Profits/Losses Change
        pandl_change = int(row["Profit/Losses"]) - previous_pandl
        previous_pandl = int(row["Profit/Losses"])
        pandl_change_list = pandl_change_list + [pandl_change]

        #Calculate the Average Profits/Losses Change
        

        #Calculate greatest increase
        #Tracking Greatests
        increase_greatest = ["", 0]
        decrease_greatest = ["", float('inf')]

        if (pandl_change > increase_greatest[1]):
            increase_greatest[0] = row["Date"]
            increase_greatest[1] = pandl_change

        #Calculate greatest decrease
        if (pandl_change < decrease_greatest[1]):
            decrease_greatest[0] = row["Date"]
            decrease_greatest[1] = pandl_change


