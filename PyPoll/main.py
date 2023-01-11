#Script analyzes records to calculate each of the following:
#* The total number of votes cast
#* A complete list of candidates who received votes
#* The percentage of votes each candidate won
#* The total number of votes each candidate won
#* The winner of the election based on popular vote.
#Also, exports a text file with the results

# Modules
import os
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

#NOTE: The above can also be run like the commented line below (I kept them separate above so that you can see what each part the code is doing):
#indi_votes = election_data.groupby('Candidate').size().to_frame(name = 'Votes').reset_index()

#Create a percentage column
percent_votes = round(((indi_votes["Votes"]/tot_votes)*100),3)
indi_votes["Percentage"] = percent_votes

#Great! Now we have a dataset to pull values from for the output

#Find max votes and its corresponding month
max_dat = indi_votes[indi_votes.Votes == indi_votes.Votes.max()]
for row in max_dat.values: 
    max_Candidate = row[0]

#Print data in terminal

#Pass the message you want for the total number of votes into a variable called "message1"
#NOTE: I wanted the code for the text to be indented the same, so I used f', but you could also use f''' here instead of repeating f' and writing \n for a new line
message1 = (
    f'Election Results'
    f'\n-------------------------'
    f'\nTotal Votes: {tot_votes}'
    f'\n-------------------------')

#Print message1 to terminal
print(f'\n{message1}')

#Create an empty dataset to store information based on the rows of candidates
outcome_rows = []

#For each row from start to end of indi_votes
for row in range(len(indi_votes)):

    #Write a new line in outcome_rows that says "[candidates name]: [percentage]% ([number of votes])" for the current row of data in indi_votes
     outcome_rows.append(f'{indi_votes.iloc[row, 0]}: '
     f'{indi_votes.iloc[row, 2]}% '
     f'({indi_votes.iloc[row, 1]})')

    #Print current row of data to terminal
     print(outcome_rows[row])

#Store message of who won in a variable called "message2"
message2 = (
    f'-------------------------\n'
    f'Winner: {max_Candidate}\n'
    f'-------------------------')

#Print message2 to terminal
print(f'{message2}\n')

#Write a text file called "analysis.txt" and set its path 
output_path = os.path.join("Analysis", "analysis.txt")

#With the text file open and in (w)riting mode
with open('Analysis/analysis.txt', 'w') as txtfile:
    
    #Write message1
    txtfile.write(message1)

    #Write candidate information stored in each row of outcome_rows on a new line
    for row in range(len(outcome_rows)):
        txtfile.write(f'\n{outcome_rows[row]}')
    
    #write message2
    txtfile.write(f'\n{message2}')