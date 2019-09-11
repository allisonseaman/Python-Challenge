import os
import csv

csvpath="election_data.csv"


total_votes=0
votes_k=0
votes_c=0
votes_l=0
votes_o=0


with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    header=next(csvreader)

    for row in csvreader:

        total_votes +=1

        if row[2]=="Correy":
            votes_c +=1
        elif row[2]=="Li":
            votes_l +=1
        elif row[2]=="Khan":
            votes_k +=1
        elif row[2]=="O'Tooley":
            votes_o +=1


per_c=100*(votes_c/total_votes)
per_l=100*(votes_l/total_votes)
per_k=100*(votes_k/total_votes)
per_o=100*(votes_o/total_votes)


print("Election Results")
print("-------------------------")
print(f"Total Votes:  {total_votes}")
print(f"-------------------------")
print(f"Khan: {per_k}% ({votes_k})")
print(f"Correy: {per_c}% ({votes_c})")
print(f"Li: {per_l}% ({votes_l})")
print(f"O'Tooley: {per_o}% ({votes_o})")
print("-------------------------")
print("Winner: Khan")


file = open("TextFile.txt", "w")

file.write("Election Results")
file.write("----------------------------")
file.write(f"Total Votes:  {total_votes}")
file.write("----------------------------")
file.write(f"Khan: {per_k}% ({votes_k})")
file.write(f"Correy: {per_c}% ({votes_c})")
file.write(f"Li: {per_l}% ({votes_l})")
file.write(f"O'Tooley: {per_o}% ({votes_o})")
file.write("----------------------------")
file.close()




     












    # csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

   




