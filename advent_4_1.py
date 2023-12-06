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
finResult = 0

for line in Lines:

    line = line.replace("  "," ")
    line = line.replace(" ",",")

    myNumbers = line.split(':')[1].split("|")[0].strip().split(",")
    winningNumbers = line.split(':')[1].split("|")[1].strip().split(",")
    i = 0
    for myNumber in myNumbers:
        if myNumber in winningNumbers and myNumber != "":
            print(f"{myNumber} is in {winningNumbers}")
            i += 1
    tempResult = calcWinningScore(i)
    print(f"{myNumbers} | {winningNumbers} - winningcards: {i} > {tempResult}")
    finResult += tempResult
    print(f"Ergebnis: {finResult}")

print(finResult)

