import os
import csv

csvpath = os.path.join('.', 'Resources', 'election_data.csv')

#Define Fieldnames
fieldnames = ["Ballot", "ID", "County", "Candidates"]

#Define list
votes_delta = []
candidates_with_votes = []

#Starting Point for future math
votes_counted = 0
candidates_counted = 0


# Method 1: Plain Reading of CSV files
with open(csvpath, 'r') as voting_data:
      reader = csv.DictReader(voting_data, fieldnames=fieldnames)
      next(reader) #Skip the header row
      for row in reader:
            
            #Calculating The total number of votes cast
            votes_counted += 1
            votes_delta.append(row["Ballot"])
            final_tally = len(votes_delta)

            #Calculating Candidates receiving votes
            

#Create Terminal Output
output = (
    f"Total Votes: {final_tally}")
    
print(output)
