# import csv file
import csv

#variables, lists, dictionaries, strings, etc
totalVotes = 0
candidateChoices = []
candidateVotes = {}
winningCandidate = ""
winningCount = 0
winningPercentage = 0

#open and read csv file
with open('election_data.csv', newline='') as electionData:
    fileReader = csv.reader(electionData)

#store header so it doesn't include into candidate data
    headers = next(fileReader)

#iterating through the data to find the
# total votes and the names of candidates
    for i in fileReader:

        totalVotes +=1

        candidateName = i[2]

        if candidateName not in candidateChoices:

            candidateChoices.append(candidateName)

            candidateVotes[candidateName] = 0

        candidateVotes[candidateName] += 1

#prepping data to be printed, specifically the total votes
    report = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {totalVotes:,}\n"
        f"-------------------------\n")
    print(report)

#finding the percentage of votes by iterating through the csv data
 #writing to txt file
with open('readme.txt', 'w') as f:
    f.write(report)
    for candidateName in candidateVotes:

        votes = candidateVotes[candidateName]

        votePercentage = float(votes) / float(totalVotes) * 100

        candidateResults = (f"{candidateName}: {votePercentage:.1f}% ({votes:,})\n")
#printing the perecentage
        print(candidateResults)
        f.write(candidateResults)
        if (votes > winningCount) and (votePercentage > winningPercentage):

            winningCount = votes
            winningPercentage = votePercentage

            winningCandidate = candidateName
#prepping winning candidate data to be printed
    summary = (
        f"Winner: {winningCandidate}\n")
    #print to terminal for winning candidate result
    print(summary)
    f.write(summary)

