#Your task is to create a Python script that analyzes the records to calculate each of the following:
# * The total number of months included in the dataset
# * The net total amount of "Profit/Losses" over the entire period
# * The changes in "Profit/Losses" over the entire period, and then the average of those changes
# * The greatest increase in profits (date and amount) over the entire period
# * The greatest decrease in profits (date and amount) over the entire period

# Modules
import os
import csv
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
d_change.drop(0,axis=0,inplace=True)

#Create a list of months
m_change = budget_data['Date']

#Drop first month because its not a part of our differences data
m_change.drop(0,axis=0,inplace=True)

#Merge differences lists into a new dataframe
diff_dat = pd.DataFrame(list(zip(m_change,d_change)), columns= ['Date','Diff'])

#Get max change and its corresponding month
max_dat = diff_dat[diff_dat.Diff == diff_dat.Diff.max()]
for row in max_dat.values: 
    max_date = row[0]
    max_value = int(row[1])

#Get min change
min_dat = diff_dat[diff_dat.Diff == diff_dat.Diff.min()]
for row in min_dat.values: 
    min_date = row[0]
    min_value = int(row[1])

#get the average
d_avg = round(diff_dat['Diff'].sum()/len(diff_dat),2)

#Print data
print(f'```text\nFinancial Analysis\n----------------------------\nTotal Months: {months}\nTotal: ${d_sum}\nAverage Change: ${d_avg}\nGreatest Increase in Profits: {max_date} (${max_value})\nGreatest Decrease in Profits: {min_date} (${min_value})\n```')
