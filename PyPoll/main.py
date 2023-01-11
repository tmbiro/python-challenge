#Script analyzes records to calculate each of the following:
#* The total number of votes cast
#* A complete list of candidates who received votes
#* The percentage of votes each candidate won
#* The total number of votes each candidate won
#* The winner of the election based on popular vote.
#Also, exports a text file with the results

# Modules
import pandas as pd

# Read the csv file
election_data = pd.read_csv('Resources/election_data.csv')

#Count total number of votes cast
tot_votes = len(election_data)

#Group by candidates
candidates = election_data.groupby('Candidate')

#Get the individual vote totals for each candidate
indi_votes = candidates.size()

#Add a name to the votes column
indi_votes = indi_votes.to_frame(name = 'Votes')

#The first column with the candidate names is being treated like and index
#We'll have to reset it to get a data column with the names
indi_votes = indi_votes.reset_index()

#NOTE: The above can also be run like below, I kept them separate above so that you can see what each part the code is doing:
#indi_votes = election_data.groupby('Candidate').size().to_frame(name = 'Votes').reset_index()

#Create a percentage column
percent_votes = round(((indi_votes["Votes"]/tot_votes)*100),3)
indi_votes["Percentage"] = percent_votes

#Great! Now we have a dataset to pull values from for the output

#Find max votes and its corresponding month
max_dat = indi_votes[indi_votes.Votes == indi_votes.Votes.max()]
for row in max_dat.values: 
    max_Candidate = row[0]

#Print data

#Create an empty dataset to store information based on the rows of candidates
outcome_rows = []

#Print the total number of votes
print(f'\nElection Results\n-------------------------\nTotal Votes: {tot_votes}\n-------------------------')

#Print each candidate's name, percentage of votes, and number of votes each on a new line
for row in range(len(indi_votes)):
     outcome_rows.append(f"{indi_votes.iloc[row, 0]}: {indi_votes.iloc[row, 2]}% ({indi_votes.iloc[row, 1]})")
     print(outcome_rows[row])

#Print who won
print(f'-------------------------\nWinner: {max_Candidate}\n-------------------------')
