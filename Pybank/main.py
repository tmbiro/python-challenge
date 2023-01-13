#Tifani Biro, January 2023
#Script analyzes the records to calculate each of the following:
# * The total number of months included in the dataset
# * The net total amount of "Profit/Losses" over the entire period
# * The changes in "Profit/Losses" over the entire period, and then the average of those changes
# * The greatest increase in profits (date and amount) over the entire period
# * The greatest decrease in profits (date and amount) over the entire period
#Also, outputs calculations to a text file

# Modules
from pathlib import Path
from textwrap import dedent
import pandas as pd

# Read the csv file in an os and pc friendly format
budget_data = pd.read_csv(Path(__file__).parent/'Resources/budget_data.csv')

#Count months
months = len(budget_data['Date'])

#Get sum of profits/losses
d_sum = budget_data['Profit/Losses'].sum()

d_change = (
    budget_data['Profit/Losses']
    .diff() #Create a list containing differences between months (.diff subtracts row 1 - row 2)
    .rename("Diff") #Rename column "Diff"
    .drop(0,axis=0) #Drop the first row of the differences list, since it only contains nan values
)

#Create a list of months
m_change = (
    budget_data['Date']
   .drop(0,axis=0) #Drop first row like we did with the differences data
) 

#Merge differences lists into a new dataframe
diff_dat = (
    pd.merge(
        m_change,
        d_change, 
        left_index=True, 
        right_index=True
    )
)


#Get max change and its corresponding month
max_change = diff_dat[diff_dat.Diff == diff_dat.Diff.max()]
max_date, max_value = max_change.values[0]

#Get min change
min_change = diff_dat[diff_dat.Diff == diff_dat.Diff.min()]
min_date, min_value = min_change.values[0]

#Get the average
d_avg = round(diff_dat['Diff'].mean(),2)

#Pass the text you want through a variable called "message" first
message = dedent(f'''
    Financial Analysis
    ----------------------------
    Total Months: {months}
    Total: ${d_sum}
    Average Change: ${d_avg}
    Greatest Increase in Profits: {max_date} (${int(max_value)})
    Greatest Decrease in Profits: {min_date} (${int(min_value)})''')

#Print message to terminal
print(f'{message}\n')

#With the text file open and ready to be (w)ritten on
with open(Path(__file__).parent/'Analysis/analysis.txt', 'w') as txtfile:    
    
    #Write the message to the text file
    txtfile.write(message)