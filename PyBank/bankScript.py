import csv
import os

csvPath = os.path.join(".", "Resources", "budget_data.csv")
writePath = os.path.join(".", "Resources", "financial_results.txt")

textOutputList = []

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

textOutputList.append("Financial Analysis")
textOutputList.append("-" * 20)
textOutputList.append(finalText.format(months = lineCount, total = runningTotal, average = average, highestMonth = highestMonth, highestAmount = greatestIncrease, lowestMonth = lowestMonth, lowestAmount = greatestDecrease))

with open(writePath, 'w') as textfile:
    for text in textOutputList:
        textfile.write(text)
        print(text)
    textfile.close()