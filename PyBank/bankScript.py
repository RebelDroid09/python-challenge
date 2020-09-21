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

    for row in lineReader:
        if lineCount > 0:
            try:
                convertedValue = int(row[1])
                runningTotal += convertedValue

                print(convertedValue)

                if convertedValue > greatestIncrease:
                    greatestIncrease = convertedValue
                elif convertedValue < greatestDecrease:
                    greatestDecrease = convertedValue     
            except ValueError:
                pass     
        print(row)
        lineCount += 1

if lineCount > 0:
    average = runningTotal / (lineCount - 1)

print(lineCount)
print(runningTotal)
print(average)
print(greatestIncrease)
print(greatestDecrease)

finalText = "Total Months: {months} Total: ${total} Average Change: ${average}2 Greatest Increase in Profits: {highestMonth} (${highestAmount}) Greatest Decrease in Profits: {lowestMonth} (${lowestMonth}) "
print()