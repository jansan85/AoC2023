def replaceWrittenNumbers(line:str):  
    REPLACEMENTS = [
        ("  1 ", " 01 "),
        ("  2 ", " 02 "),
        ("  3 ", " 03 "),
        ("  4 ", " 04 "),
        ("  5 ", " 05 "),
        ("  6 ", " 06 "),
        ("  7 ", " 07 "),
        ("  8 ", " 08 "),
        ("  9 ", " 09 ")
    ]
    for old, new in REPLACEMENTS:
        line = line.replace(old, new)
    return line


def calcWinningScore(i):
    if i == 0:
        return 0
    else:
        result = 1
        i -= 1
    while not i == 0:
        result = result * 2
        i -= 1
    return result

############ MAIN ###################################

file1 = open(r'C:\WorkSpace\aoc2023\input4.txt', 'r')
Lines = file1.readlines()
result = 0

multiplier = [1 for i in Lines]

for count, line in enumerate(Lines):
    line = line.replace("  "," ")
    line = line.replace(" ",",")

    myNumbers = line.split(':')[1].split("|")[0].strip().split(",")
    winningNumbers = line.split(':')[1].split("|")[1].strip().split(",")
    cardsWon = 0
    # get number of won cards
    for myNumber in myNumbers:
        if myNumber in winningNumbers and myNumber != "":
            cardsWon += 1
    # increase number of won cards for left to play cards
    while cardsWon > 0:
        multiplier[count+cardsWon] += multiplier[count] #multiply wins by number of card copies
        cardsWon =  cardsWon-1   

# get sum of all cards and copies
for gameIndex, j in enumerate(multiplier):
    result += multiplier[gameIndex]

print(result)

