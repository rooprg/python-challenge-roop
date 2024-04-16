# Import the os module and the module for reading CSV files
import os
import csv

csvpath = os.path.join('.', 'Resources', 'budget_data.csv')

#Define the field names for two columns
fieldnames = ['Date', 'Profit/Losses']

# Generating output
file_to_output = "PyBank Analysis Summary"

#Create lists
delta_months = []
revenue_change_list = []

#Starting points for future math
months_total = 0
previous_revenue = 0
revenue_total = 0

#Tracking Greatests
increase_greatest = ["", 0]
decrease_greatest = ["", float('inf')]

# Read the csv and convert it into a dictionary using DictReader
with open(csvpath) as financial_data:
    reader = csv.DictReader(financial_data, fieldnames=fieldnames)
    next(reader)  # Skip the header row
    for row in reader:

        #Change in Months calculation
        months_total += 1
        delta_months.append(row["Date"])

        #Total revenue calculation
        revenue_total = revenue_total + int(row["Profit/Losses"])

        #Calculate Revenue Change
        revenue_change = int(row["Profit/Losses"]) - previous_revenue
        previous_revenue = int(row["Profit/Losses"])
        revenue_change_list = revenue_change_list + [revenue_change]

        #Calculate the Average Revenue Change
        average_change = sum(revenue_change_list) / len(revenue_change_list)

        #Calculate greatest increase

        #Calculate greatest decrease

output = (
    f"Financial Analysis\n"
    f"----------------------------------\n"
    f"Total Months: {months_total}\n"
    f"Total Revenue: ${revenue_total}\n")
    
print(output)

#Outputing a .txt file
