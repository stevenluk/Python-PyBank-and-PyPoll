import csv
import os

#initialize necessary values and lists
rows=0
totalrevenue=0
revenuechange=0
initialrevenue=0
changeinrevenue=[]
date=[]

#set path for file
dir_path=os.path.dirname(os.path.realpath(__file__))
csvpath=os.path.join(dir_path,'budget_data.csv')

#open csv file
with open('budget_data.csv', 'r') as csvfile:
    Data = csv.reader(csvfile,delimiter=',')
    next(Data)

 #iterate through all lines to get total revenue and revenue change 
    for lines in Data:
        rows +=1
       
        totalrevenue=totalrevenue+int(lines[1])
        difference=int(lines[1])-int(initialrevenue)
        changeinrevenue.append(difference)
        date.append(lines[0])
        revenuechange=revenuechange+difference
        initialrevenue=lines[1]

 #calculate average, max and min of revenue       
averagechange=revenuechange/rows     
maxincrease=max(changeinrevenue)
maxincreasedate=date[changeinrevenue.index(maxincrease)]
maxdecrease=min(changeinrevenue)
maxdecreasedate=date[changeinrevenue.index(maxdecrease)]

#print out results in terminal
print("Finicial Analysis")
print("----------------------------")
print("Total Months: " + str(rows))
print("Total: " + "$" + str(totalrevenue))
print("Average Change: " + "$" + str(averagechange))
print("Greatest Increase in Profits:" + str(maxincreasedate) + " ($" + str(maxincrease) + ")")
print("Greatest Decrease in Profits:" + str(maxdecreasedate) + " ($" + str(maxdecrease) + ")")

#create an output txt file with the results
file=open("Financial Analysis.txt","w")

file.write(str("Financial Analysis") + "\n")
file.write(str("----------------------------") + "\n")
file.write(str("Total Months: " + str(rows)) + "\n")
file.write(str("Total: " + "$" + str(totalrevenue)) + "\n")
file.write(str("Average Change: " + "$" + str(averagechange)) + "\n")
file.write(str("Greatest Increase in Profits:" + str(maxincreasedate) + " ($" + str(maxincrease) + ")") + "\n")
file.write(str("Greatest Decrease in Profits:" + str(maxdecreasedate) + " ($" + str(maxdecrease) + ")") + "\n")
file.close