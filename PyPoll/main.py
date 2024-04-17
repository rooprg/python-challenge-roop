import os
import csv

csvpath = os.path.join('.', 'Resources', 'election_data.csv')

# Total Vote Counter
total_votes = 0

# Candidates Options and Vote Counters
candidate_options = []
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0

# Method 1: Plain Reading of CSV files
with open(csvpath, 'r') as voting_data:
    reader = csv.DictReader(voting_data)
    
    for row in reader:
        # Add to the total vote count
        total_votes = total_votes + 1
        
        # Extract the candidate name from each row
        candidate_name = row["Candidate"]
        
        # If the candidate does not match any existing candidate
        if candidate_name not in candidate_options:
            # Add it to the list of candidates in the running
            candidate_options.append(candidate_name)
            # And begin tracking that candidate's voter count
            candidate_votes[candidate_name] = 0
        
        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

# Determine the winner by looping through the counts
for candidate in candidate_votes:
    # Retrieve the vote count and percentage
    votes = candidate_votes.get(candidate)
    vote_percentage = float(votes) / float(total_votes) * 100
    
    # Determine winning vote count and candidate
    if votes > winning_count:
        winning_count = votes
        winning_candidate = candidate

# Create Terminal Output
output = (
    f"Election Results\n"
    f"--------------------------\n"
    "\n"
    f"Total Votes: {total_votes}\n"
    "\n"
    f"--------------------------\n"
)

for candidate in candidate_votes:
    votes = candidate_votes[candidate]
    vote_percentage = float(votes) / float(total_votes) * 100
    output += f"{candidate}: {vote_percentage:.3f}% ({votes})\n"

output += (
    f"\n"
    f"--------------------------\n"
    "\n"
    f"Winner: {winning_candidate}\n"
    "\n"
    f"--------------------------\n"
)

print(output)