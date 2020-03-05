import csv
import os
from collections import Counter

#set path for file
dir_path=os.path.dirname(os.path.realpath(__file__))
csvpath=os.path.join(dir_path,'election_data.csv')

#initialize necessary values and lists
rows=0
candidate=[]

#open csv file
with open('election_data.csv', 'r') as csvfile:
     Data = csv.reader(csvfile,delimiter=',')
     next(Data)

#iterate through all lines to get all candidates
     for lines in Data:
         rows += 1
         candidate.append(lines[2])

#count each candidate's counts and store in a dictionary
result=[]
newcandidate=dict(Counter(candidate))
for i in newcandidate.keys():
    result.append(i)
    result.append(newcandidate[i])

#get each candidate's name and count
candidate1=result[0]
votes1=result[1]
candidate2=result[2]
votes2=result[3]
candidate3=result[4]
votes3=result[5]
candidate4=result[6]
votes4=result[7]

#calculate percentage of each candidate
candidate1percentage=format(votes1/rows,".3%")
candidate2percentage=format(votes2/rows,".3%")
candidate3percentage=format(votes3/rows,".3%")
candidate4percentage=format(votes4/rows,".3%")

#store all candidates' percentages in a list
num=[]
num.append(candidate1percentage)
num.append(candidate2percentage)
num.append(candidate3percentage)
num.append(candidate4percentage)

#store all candidates' names in a list
name=[]
name.append(candidate1)
name.append(candidate2)
name.append(candidate3)
name.append(candidate4)

#find the winner of the candidate
winnernum=max(num)
position=num.index(winnernum)
winner=name[position]

#print out result in the terminal
print("Election Results")
print("----------------------------")
print("Total Votes: " + str(rows))
print("----------------------------")
print(candidate1 + ": " + str(candidate1percentage) + " " + "(" + str(votes1) + ")")
print(candidate2 + ": " + str(candidate2percentage) + " " + "(" + str(votes2) + ")")
print(candidate3 + ": " + str(candidate3percentage) + " " + "(" + str(votes3) + ")")
print(candidate4 + ": " + str(candidate4percentage) + " " + "(" + str(votes4) + ")")
print("----------------------------")
print("Winner: " + winner)
print("----------------------------")


#create an output txt file with the result
file=open("Election Results.txt","w")

file.write(str("Election Results") + "\n")
file.write(str("----------------------------") + "\n")
file.write(str("Total Votes: " + str(rows)) + "\n")
file.write(str("----------------------------") + "\n")
file.write(candidate1 + ": " + str(candidate1percentage) + " " + "(" + str(votes1) + ")" + "\n")
file.write(candidate2 + ": " + str(candidate2percentage) + " " + "(" + str(votes2) + ")" + "\n")
file.write(candidate3 + ": " + str(candidate3percentage) + " " + "(" + str(votes3) + ")" + "\n")
file.write(candidate4 + ": " + str(candidate4percentage) + " " + "(" + str(votes4) + ")" + "\n")
file.write(str("----------------------------") + "\n")
file.write("Winner: " + winner + "\n")
file.write(str("----------------------------") + "\n")
file.close