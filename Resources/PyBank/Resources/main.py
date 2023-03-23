# import csv file
import csv

#open and read csv file
with open('budget_data.csv', newline='') as csvfile:
    csvData = list(csv.reader(csvfile))

#store header (without this, it will affect the data input)
    csvData.pop(0)

#empty lists
months = []
profitLoss =[]
changes=[]
splitMax=[]

#take list and pull out each entry before - and make a new list based on that data
for i in range(len(csvData)):

# The total number of months included in the dataset
#this makes sure months list will only have unique items
    if csvData[i][0] not in months:
        months.append(csvData[i][0])

# The net total amount of "Profit/Losses" over the entire period
    if csvData[i][1] not in profitLoss:
        profitLoss.append(int(csvData[i][1]))

# The changes in "Profit/Losses" over the entire period, and then the average of those changes
changes = [profitLoss[i+1]-profitLoss[i] for i in range(len(profitLoss)-1)]

# Python program to get average of a list
def Average(changes):
    return sum(changes) / len(changes)

average = Average(changes)

# The greatest increase in profits (date and amount) over the entire period
#if statement. If the max in changes list is [0], then print csvData[0]
#first find max, then find min
maxValue = max(changes)
index = changes.index(maxValue)
# print(index) #use this index number to find which is max and thn use CSVdata corresponding index
# print(splitMax[0])

# The greatest decrease in profits (date and amount) over the entire period
minValue = min(changes)
minIndex = changes.index(minValue)
# print(minIndex)

# Function to convert
def convert(csvData):

    # initialize an empty string
    str1 = " "

    # return string
    return (str1.join(csvData[79]))

# Function to convert
def convertMin(csvData):

    # initialize an empty string
    str1 = " "

    # return string
    return (str1.join(csvData[49]))

#finding the max and min of the data
splitMax = convert(csvData).split(" ")[0]
splitMin = convertMin(csvData).split(" ")[0]

#print commands
# print(f'Total number of months: {len(months)}')
# print(f'Net profit/loss changes: ${sum(profitLoss)}')
# # Printing average of the list
# print("Average changes in profit/loss=", round(average, 2))
# print(f'Greatest Increase in Profits: {splitMax} ({maxValue})')
# print(f'Greatest Decrease in Profits: {splitMin} ({minValue})')

#prepping the data to be printed
report = (f"\
Total number of months: {len(months)}\n\
Net profit/loss changes: ${sum(profitLoss)}\n\
Average changes in profit/loss: {round(average, 2)}\n\
Greatest Increase in Profits: {splitMax} ({maxValue})\n\
Greatest Decrease in Profits: {splitMin} ({minValue})"
)

#print statment for terminal
print(report)

#writing to txt file
with open('readme.txt', 'w') as f:
    f.write(report)





