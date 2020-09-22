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
    winnerIndex = ""
    winnerTotal = 0

    for row in lineReader:
        if lineCount > 0:
            try:
                voterId = row[0]
                voterCount = row[1]
                voterCandidate = row[2]

                voteTotal += 1

                if not voterCandidate in candidateList:
                    candidateList.append(voterCandidate)

                candidateLength = len(candidateList)
                candidateVoteLength = len(candidateTotalVotes)

                if candidateLength > candidateVoteLength:
                    candidateTotalVotes.append(1)
                else:
                    candidateIndex = candidateList.index(voterCandidate)
                    candidateTotalVotes[candidateIndex] += 1                
            except ValueError:
                pass     
                print("something went wrong in the main election tally.")
       
        lineCount += 1

if voteTotal > 0:
    for candidate in candidateList:
        candidateIndex = candidateList.index(candidate)
        candidatePercentage = (candidateTotalVotes[candidateIndex] / voteTotal) * 100
        candidatePercentageList.append(candidatePercentage)

        if winnerTotal < candidateTotalVotes[candidateIndex]:
            winnerTotal = candidateTotalVotes[candidateIndex]
            winner = candidate


print("Election Results")
print("-" * 20)
print("Total Votes: {votes}".format(votes = voteTotal))
print("-" * 20)
if voteTotal > 0:
    for candidate in candidateList:
        candidateIndex = candidateList.index(candidate)
        print("{Name}: %{percent:.3f} ({voteCount})".format(Name = candidate, percent = candidatePercentageList[candidateIndex], voteCount = candidateTotalVotes[candidateIndex]))
print("-" * 20)
print("Winner: {winner}".format(winner = winner))
print("-" * 20)