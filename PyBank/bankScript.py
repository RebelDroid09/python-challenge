import csv

with open('Resources\budget_data.csv', newline='') as csvfile:
    lineReader = csv.reader(csvfile, delimiter=',')

    lineCount = 0
    runningTotal = 0
    average = 0
    greatestIncrease = 0
    greatestDecrease = 0

    for row in lineReader:
        if lineCount == 0:
            pass
        else:
            if isnumeric(row[1]):
                runningTotal += row[1]

                if row[1] > greatestIncrease:
                    greatestIncrease = row[1]
                elif row[1] < greatestDecrease:
                    greatestDecrease = row[1]

            lineCount += 1

average = runningTotal / lineCount