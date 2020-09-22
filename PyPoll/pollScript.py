import csv
import os

csvPath = os.path.join(".", "Resources", "election_data.csv")

with open(csvPath) as csvfile:
    lineReader = csv.reader(csvfile, delimiter=',')

    lineCount = 0
    voteTotal = 0
    candidateList = []
    candidateTotalVotes = []
    candidatePercentageList = []    
    electionWinner = ""

    for row in lineReader:
        if lineCount > 0:
            try:
                voterId = row[0]
                voterCount = row[1]
                voterCandidate = row[2]

                voteTotal += 1

                if not voterCandidate in candidateList:
                    candidateList.append(voterCandidate)

                if len(candidateList) <> len(candidateTotalVotes):
                    candidateTotalVotes.append(1)
                else:
                    candidateIndex = candidateList.index(voterCandidate)
                    candidateTotalVotes[candidateIndex] += 1                
            except ValueError:
                pass     
       
        lineCount += 1

if voteTotal > 0:
    for candidate in candidateList:
        candidateIndex = candidateList.index(candidate)
        candidatePercentage = (candidateTotalVotes[candidateIndex] / voteTotal) * 100
        candidatePercentageList.append(candidatePercentage)

# finalText = "Total Months: {months} Total: ${total} Average Change: ${average:.2f} Greatest Increase in Profits: {highestMonth} (${highestAmount}) Greatest Decrease in Profits: {lowestMonth} (${lowestAmount})"

# print("Financial Analysis")
# print("-" * 20)
# print(finalText.format(months = lineCount, total = runningTotal, average = average, highestMonth = highestMonth, highestAmount = greatestIncrease, lowestMonth = lowestMonth, lowestAmount = greatestDecrease))