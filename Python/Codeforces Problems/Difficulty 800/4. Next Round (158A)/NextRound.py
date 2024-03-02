okay = str(input())
veryokay = okay.split()
totalPassCounter  = 0
totalcontestants = int(veryokay[0])
minimumScore = int(veryokay[1])

inputContestantScore = str(input())
ContestantScoreList = inputContestantScore.split()

ContestantScore1 = [int(element) for element in ContestantScoreList]
minimumScoreContestant = ContestantScore1[minimumScore-1]

for i in ContestantScore1:
    if i == 0:
        break
    elif i >= minimumScoreContestant:
        totalPassCounter = totalPassCounter + 1

print(totalPassCounter)
