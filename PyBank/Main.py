import os

# Module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

total_month=0
net_change=0
avg_change=0
net_changelist=[]
# Method 2: Improved Reading using CSV module

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    jan_data=next(csvreader)
    total_month=total_month+1
    net_change=net_change+int(jan_data[1])
    previous_change=int(jan_data[1])




    # Read each row of data after the header
    for row in csvreader:
        #print(row)
        total_month=total_month+1
        net_change=net_change+int(row[1])
        change=int(row[1])-previous_change
        previous_change=int(row[1])
        net_changelist.append(change)

avg_change=sum(net_changelist)/len(net_changelist)
print(total_month,net_change,round(avg_change,2))