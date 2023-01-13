#Tifani Biro, January 2023
#Script analyzes the records to calculate each of the following:
# * The total number of months included in the dataset
# * The net total amount of "Profit/Losses" over the entire period
# * The changes in "Profit/Losses" over the entire period, and then the average of those changes
# * The greatest increase in profits (date and amount) over the entire period
# * The greatest decrease in profits (date and amount) over the entire period
#Also, outputs calculations to a text file

# Modules
import os
import pandas as pd

# Read the csv file
budget_data = pd.read_csv('Resources/budget_data.csv')

#Count months
months = len(budget_data)

#Get sum of profits/losses
d_sum = sum(budget_data['Profit/Losses'])

#Create a list containing differences between months (.diff subtracts row 1 - row 2)
d_change = budget_data['Profit/Losses'].diff()

#Drop the first row of the differences list, since it only contains nan values
d_change.drop(0,axis=0)

#Create a list of months
m_change = budget_data['Date']

#Drop first month because its not a part of our differences data
m_change.drop(0,axis=0)

#Merge differences lists into a new dataframe
diff_dat = pd.DataFrame(list(zip(m_change,d_change)), columns= ['Date','Diff'])

#Get max change and its corresponding month
max_change = diff_dat[diff_dat.Diff == diff_dat.Diff.max()]
max_date, max_value = max_change.values[0]

#Get min change
min_change = diff_dat[diff_dat.Diff == diff_dat.Diff.min()]
min_date, min_value = min_change.values

#Get the average
d_avg = round(diff_dat['Diff'].mean(),2)

#Pass the text you want through a variable called "message" first
message = (
    f'Financial Analysis\n'
    f'----------------------------\n'
    f'Total Months: {months}\n'
    f'Total: ${d_sum}\n'
    f'Average Change: ${d_avg}\n'
    f'Greatest Increase in Profits: {max_date} (${int(max_value)})\n'
    f'Greatest Decrease in Profits: {min_date} (${int(min_value)}) ')

#Print message to terminal
print(f'\n{message}\n')

#Write a text file called "analysis.txt"
output_path = os.path.join("Analysis", "analysis.txt")

#With the text file open and ready to be (w)ritten on
with open('Analysis/analysis.txt', 'w') as txtfile:
    
    #Write the message to the text file
    txtfile.write(message)