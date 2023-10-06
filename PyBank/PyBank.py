import os
import sys
import csv

#Make paths for data and path for coding output

bankdata = "Resources/budget_data.csv"
outputpath = "Analysis/pybankanalysis.txt"

#Set value for total months and total dollar amount
monthtally = 0
nettotal = 0


#if there r n months then there r n-1 changes

with open(bankdata) as bank_data:
    csvreader = csv.reader(bank_data, delimiter=',')
    #skips header
    next(csvreader)

    #Counting each time a month pops up in dataset 
    Words = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    for Words in csvreader:
        monthtally += 1
    
    #Calculating net total
    for row in csvreader:
        nettotal = nettotal + row[1]

    

             

with open(outputpath, "w") as textfile:
   #Total months print
    output = (
        f"\n\nBank Analysis\n"
        f"-------------------------\n"
        f"Total Months: {monthtally}\n"
        f"-------------------------\n")
    print(output, end="")
    textfile.write(output)

    #Net total print
    #output = (
       # f"-------------------------\n"
        #f"Net Total: {nettotal}\n"
       # f"-------------------------\n")
   # print(output, end="")
    #textfile.write(output)

    #Avg change
    output = (
        f"-------------------------\n"
       # f"Average change: {[1].max()}\n"
        f"-------------------------\n")
    print(output, end="")
    textfile.write(output)
   
    #Increase
    output = (
        f"-------------------------\n"
        f"Greatest Increase in Profit: {csvreader[1].max()}\n"
        f"-------------------------\n")
    print(output, end="")
    textfile.write(output)

    #Decrease
    output = (
        f"-------------------------\n"
        f"Greatest Decrease in Profit: {csvreader[1].min()}\n"
        f"-------------------------\n")
    print(output, end="")
    textfile.write(output)

#I can't figure out how to find the net total or just figure out how to write that I want column1 and find the sum, avg., min/max
