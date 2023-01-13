#Tifani Biro, January 2023
#Script analyzes records to calculate each of the following:
#* The total number of votes cast
#* A complete list of candidates who received votes
#* The percentage of votes each candidate won
#* The total number of votes each candidate won
#* The winner of the election based on popular vote.
#Also, exports a text file with the results

# Modules
from pathlib import Path
from textwrap import dedent
import pandas as pd

# Read the csv file in a format that os and pc can read
election_data = pd.read_csv(Path(__file__).parent/'Resources/election_data.csv')

#Count total number of votes cast
tot_votes = len(election_data)

#Create a new sorted dataset with the number of votes each candidate received
indi_votes = (
    election_data
    .groupby('Candidate') #Group by candidates
    .size() #Get the individual vote totals for each candidate
    .to_frame(name = 'Votes') #Add a name to the votes column
    .reset_index()) #The first column with the candidate names is being treated like and index, so we'll reset it

#Create a percentage column and round it to 3 decimal places
indi_votes["Percentage"] = ((indi_votes["Votes"]/tot_votes)*100).round(3)

#Great! Now we have a dataset to pull values from for the output

#Find max votes and its corresponding candidate
max_dat = indi_votes[indi_votes.Votes == indi_votes.Votes.max()]
max_Candidate = max_dat["Candidate"].squeeze()

#Print data in terminal

#Pass the message you want for the total number of votes into a variable called "message1"
#NOTE: I wanted the code for the text to be indented the same, so I used f', but you could also use f''' here instead of repeating f' and writing \n for a new line
message1 = dedent(
    f'''
    Election Results
    -------------------------
    Total Votes: {tot_votes}
    -------------------------
    '''.rstrip())

#Create an empty dataset to store information based on the rows of candidates
outcome_rows = []

#For each row from start to end of indi_votes
for index,row in indi_votes.iterrows():
    outcome_rows.append(f"{row['Candidate']}: {row['Percentage']}% ({row['Votes']} votes)")

#Store message of who won in a variable called "message2"
message2 = dedent(
    f'''
    -------------------------
    Winner: {max_Candidate}
    -------------------------
    '''.rstrip())

print(message1, *outcome_rows, message2, sep="\n")

#With the text file open and in (w)riting mode for any operating system
with open(Path(__file__).parent/'Analysis/analysis.txt', 'w') as txtfile:
    
    #Write message1
    txtfile.write(f'{message1}\n')

    #Write candidate information stored in each row of outcome_rows on a new line
    txtfile.write("\n".join(outcome_rows))
    
    #write message2
    txtfile.write(message2)