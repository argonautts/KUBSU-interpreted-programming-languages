with open("file.txt", "r", encoding='utf-8') as file:
    text = file.read()
    allFile = text.split('\n')
    print("Whole file:", allFile, "\n")

    countVotes = 0
    for index in range(len(allFile)):
        if allFile[index] == "VOTES:":
            countVotes = index
            break

    parties = allFile[1:countVotes] # slice
    print("List of parties:", parties)

    votes = allFile[countVotes+1:len(allFile)]
    print("List of votes:", votes, "\n")


    votesResult = []
    votesSum = 0

    for party in parties:
        vote = 0
        for indexVotes in range(len(votes)):
            if party == votes[indexVotes]:
                vote += 1
        votesResult.append(vote)
        votesSum += vote


    result = dict(zip(parties, votesResult))
    print("Voting results = ", result, "\n")

    votesCheck = votesSum * 7 / 100
    print("Names of parties that received at least 7% of the number of votes ( out of", votesSum,"):")
    for key, value in result.items():
        if value > votesCheck:
            print(key)

'''
PARTIES:
Party one
Party two
Party three
VOTES:
Party one
Party one
Party three
Party one
Party one
Party three
Party two
Party one
Party three
Party three
Party one
Party one
Party three
Party three
Party one
'''