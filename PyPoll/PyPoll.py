# @AUTHOR: ANIKA NGUYEN
import os
import sys
import csv

#Variable of path to input data file.
pollData = "Resources/election_data.csv"
outputpath = "Analysis/pypollanalysis.txt"


#Set integers

total_votes = 0
winnercount = 0
winnername = ""
candidates = {}
# candidates["key"] = 0 -> candidates = {"key": 0}
# candidates = {"Charles Casper Stockham": 2, "Diana DeGette": 1} 
# --> Get Charles's vote count: candidates, "Charles Casper Stockham", how do I get 2
# ["Charles Casper Stockham", "Diana DeGette"]

#Open file, read, parse it by comma and count votes per users.
with open(pollData) as poll_data:
    csvreader = csv.reader(poll_data, delimiter=',')
    next(csvreader)

    for row in csvreader:
        total_votes += 1
        if row[2] in candidates.keys():
            candidates[row[2]] += 1
        else: # When the name is not in the dictionary keys
            candidates[row[2]] = 1




with open(outputpath, "w") as textfile:
    output = (
        f"\n\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n")
    print(output, end="")

    textfile.write(output)

    for candidate in candidates.keys():
        votes = candidates[candidate]
        percent = votes/total_votes * 100
    

        if votes > winnercount: 
            winnercount = votes
            winnername = candidate


        voter_output = f"{candidate}: {percent:.3f}% ({votes})\n"
        print(voter_output)

        textfile.write(voter_output)

    output = (
        f"-------------------------\n"
        f"Winner: {winnername}\n"
        f"-------------------------\n")
    print(output, end="")

    textfile.write(output)



