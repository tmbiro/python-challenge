#Script analyzes records to calculate each of the following:
#* The total number of votes cast
#* A complete list of candidates who received votes
#* The percentage of votes each candidate won
#* The total number of votes each candidate won
#* The winner of the election based on popular vote.
#Also, exports a text file with the results

# Modules
import pandas as pd
import numpy as np

# Read the csv file
election_data = pd.read_csv('Resources/election_data.csv')

#Count total number of votes cast
tot_votes = len(election_data)

#Group by candidates
candidates = election_data.groupby('Candidate')

#Get the individual vote totals for each candidate
indi_votes = candidates.size()

#Add a name to the votes column
indi_votes = indi_votes.to_frame(name ='Votes')

#Since the first column with the candidate names is being treated like and index, we'll have to reset it to get a data column with the names
indi_votes = indi_votes.reset_index()

#Create a percentage column
percent_votes = round(((indi_votes["Votes"]/tot_votes)*100),3)
indi_votes["Percentage"] = percent_votes

#Great! Now we have a dataset
#print(f'{candidates.head()}')
print(f'{indi_votes}')

