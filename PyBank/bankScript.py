import csv
import os

csvPath = os.path.join(".", "Resources", "budget_data.csv")

with open(csvPath) as csvfile:
    lineReader = csv.reader(csvfile, delimiter=',')

    lineCount = 0
    runningTotal = 0
    average = 0
    greatestIncrease = 0
    greatestDecrease = 0  
    highestMonth = ""
    lowestMonth = "" 

    for row in lineReader:
        if lineCount > 0:
            try:
                convertedValue = int(row[1])
                runningTotal += convertedValue

                if convertedValue > greatestIncrease:
                    greatestIncrease = convertedValue
                    highestMonth = row[0]
                elif convertedValue < greatestDecrease:
                    greatestDecrease = convertedValue     
                    lowestMonth = row[0]
            except ValueError:
                pass     
       
        lineCount += 1

if lineCount > 0:
    average = runningTotal / (lineCount - 1)

finalText = "Total Months: {months} Total: ${total} Average Change: ${average:.2f} Greatest Increase in Profits: {highestMonth} (${highestAmount}) Greatest Decrease in Profits: {lowestMonth} (${lowestAmount})"

print("Financial Analysis")
print("-" * 20)
print(finalText.format(months = lineCount, total = runningTotal, average = average, highestMonth = highestMonth, highestAmount = greatestIncrease, lowestMonth = lowestMonth, lowestAmount = greatestDecrease))