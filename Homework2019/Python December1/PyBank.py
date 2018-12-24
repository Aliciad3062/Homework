import os
import csv

import os
import csv

csvpath = os.path.join(".", "Resources", "budget_data.csv")
print (csvpath)

total_rows=0
net_amount= 0
average= 0
max_inc= 0
max_date= " "
min_inc= 1170593
min_date= " "


# Read in the CSV file
with open(csvpath, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    print(header)

    for row in csvreader:
        #print(row[0],row[1])
        total_rows=total_rows+1
        net_amount=net_amount + int(row[1])
        if int(row[1]) > max_inc:
            max_inc=(int(row[1]))
            max_date = row[0]
        if total_rows == 1:
            min_inc = int(row[1])
            max_inc = int(row[1])
        if int(row[1])< min_inc:
            min_inc = int(row[1])
            min_date = row[0]



    print (total_rows)
    print(net_amount)
    print(net_amount/total_rows)
    print (max_inc, max_date)
    print(min_inc, min_date)






