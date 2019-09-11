import os
import csv

csvpath="budget_data.csv"

with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    Profit=[]
    Months=[]
    

    for row in csvreader:
        print(row)
        Months.append(row[0])
        Profit.append(int(row[1]))

    change_rev=[]

    for x in range(1, len(Profit)):
        change_rev.append((int(Profit[x]) - int(Profit[x-1])))



    Months_length=len(Months)
    Total_Profit=sum(Profit)
    Average_Revenue=sum(change_rev) / len(change_rev)
    greatest_inc=max(change_rev)
    greatest_dec=min(change_rev)


    print("Financial Analysis:")
    print("----------------------------")
    print("Total Months: " + str(Months_length))
    print("Total: " + "$" + str(Total_Profit))
    print("Average Change: " + "$" + str(Average_Revenue))
    print("Greatest Increase in Profits: " + str(greatest_inc))
    print("Greatest Decrease in Profits: " + str(greatest_dec))




    file = open("TextFile.txt", "w")



    file.write("Financial Analysis:")
    file.write("----------------------------")
    file.write("Total Months: " + str(Months_length))
    file.write("Total: " + "$" + str(Total_Profit))
    file.write("Average Change: " + "$" + str(Average_Revenue))
    file.write("Greatest Increase in Profits: " + str(greatest_inc))
    file.write("Greatest Decrease in Profits: " + str(greatest_dec))
    file.close()

   








