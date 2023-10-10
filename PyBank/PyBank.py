import os
import sys
import csv

#Make paths for data and path for coding output

bankdata = "Resources/budget_data.csv"
outputpath = "Analysis/pybankanalysis.txt"

#Set value for total months and total dollar amount
monthtally = 0
nettotal = 0
prev = 0
changes = []


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
    # for row in csvreader:
        nettotal = nettotal + int(Words[1])
        change = int(Words[1]) - prev 

        prev = int(Words[1])

        changes.append(change)
#remove item using index --> not in for loop
del changes[1]

avgchange = sum(changes)/len(changes)



        

    

             

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
    output = (
        f"-------------------------\n"
        f"Net Total: {nettotal}\n"
       f"-------------------------\n")
    print(output, end="")
    textfile.write(output)

    #Avg change
    output = (
        f"-------------------------\n"
        f"Average change: {avgchange}\n"
        f"-------------------------\n")
    print(output, end="")
    textfile.write(output)
   
    #Increase
    output = (
        f"-------------------------\n"
        f"Greatest Increase in Profit: {max(changes)}\n"
        f"-------------------------\n")
    print(output, end="")
    textfile.write(output)

    #Decrease
    output = (
        f"-------------------------\n"
        f"Greatest Decrease in Profit: {min(changes)}\n"
        f"-------------------------\n")
    print(output, end="")
    textfile.write(output)

#avg is different from result on module hw?
