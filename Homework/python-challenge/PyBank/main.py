#PyBank Jackie

#Import os mod and mod for reading files
import os
import csv

#Load files and output path
csvpath = os.path.join('budget_data.csv')
pathout = "Output/Bank.txt"

#Set Variables
month_count = 0
amount = 0
prior = 0
monthly_change = []
increase = 0
decrease = 0 

#Open CSV, list of dictionaries
with open(csvpath) as revenue:
    reader = csv.DictReader (revenue)

    for row in reader:
    #int to track total
        month_count = month_count + 1
        amount = amount + int (row['P/L'])

        if month_count > 1 :
            change=int (row['P/L'])-prior
            month_count.append(change)

            if change > increase :
                increase = change 
                increaseMonth = row['Date']

            if change > decrease :
                decrease = change
                decreaseMonth = row['Date']
    prior=int (row['P/L'])
average = (sum(monthly_change)/len(monthly_change)

output=(str
    'Total number of months=' + str(month_count)+'\n'
    'Total net amount of P/L = ' + str(amount)+'\n'  
    'Average change in P/L between months = ' + str(average)+ '\n'
    'The greatest increase in profits (date and amount)=' + (increaseMonth) + '$'+str(increase) + '\n' 
    'The greatest decrease in losses (date and amount)=' + (decreaseMonth) + '$'+str(decrease) + '\n'
)

print(output)

with open (pathout, 'w') as txt_file
    text_file.write(output)




        





















