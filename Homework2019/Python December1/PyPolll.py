import os
import csv

election_csv = os.path.join('.', 'election_data.csv')

total_votes = 0
candidates = []
khan_total = 0
correy_total = 0
li_total = 0
otooley_total=0
winner_total = 0


with open(election_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    header = next(csvreader)

    for row in csvreader:
        total_votes += 1
        if row[2] not in candidates:
            candidates.append(row[2])
        if row[2] == "Khan":
            khan_total += 1
        if row[2] == "Correy":
            correy_total += 1
        if row[2] == "Li":
            li_total += 1
        if row[2] == "O'Tooley":
            otooley_total += 1

    percent_khan = "{:.2%}".format(khan_total / total_votes)
    percent_correy = "{:.2%}".format(correy_total / total_votes)
    percent_li = "{:.2%}".format(li_total / total_votes)
    percent_otooley = "{:.2%}".format(otooley_total / total_votes)

    if khan_total > winner_total:
        winner_total = khan_total
        winner = "Khan"
    if correy_total > winner_total:
        winner_total = correy_total
        winner = "Correy"
    if li_total > winner_total:
        winner_total = li_total
        winner = "Li"
    if otooley_total > winner_total:
        winner_total = otooley_total
        winner = "O'Tooley"


    print("Election Results")
    print("-----------------------------------")
    print(f"Total Votes: {total_votes}")
    print("-----------------------------------")
    print(f"Khan: {percent_khan} ({khan_total})")
    print(f"Correy: {percent_correy} ({correy_total})")
    print(f"Li: {percent_li} ({li_total})")
    print(f"O'Tooley: {percent_otooley} ({otooley_total})")
    print("-----------------------------------")
    print(f"Winner: {winner}")
    print("-----------------------------------")

file = open("output_file_main2.txt", "w")
file.write("Election Results\n")
file.write("-----------------------------------\n")
file.write(f"Total Votes: {total_votes}\n")
file.write("-----------------------------------\n")
file.write(f"Khan: {percent_khan} ({khan_total})\n")
file.write(f"Correy: {percent_correy} ({correy_total})\n")
file.write(f"Li: {percent_li} ({li_total})\n")
file.write(f"O'Tooley: {percent_otooley} ({otooley_total})\n")
file.write("-----------------------------------\n")
file.write(f"Winner: {winner}\n")
file.write("-----------------------------------\n")
file.close()