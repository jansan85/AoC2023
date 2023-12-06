def replaceWrittenNumbers(line:str):  
    REPLACEMENTS = [
        ("one", "one1one"),
        ("two", "two2two"),
        ("three", "three3three"),
        ("four", "four4four"),
        ("five", "five5five"),
        ("six", "six6six"),
        ("seven", "seven7seven"),
        ("eight", "eight8eight"),
        ("nine", "nine9nine")
    ]
    for old, new in REPLACEMENTS:
        line = line.replace(old, new)
    return line


######### MAIN #######

file1 = open(r'C:\WorkSpace\aoc2023\input1.txt', 'r')
Lines = file1.readlines()
firstDigit = 0
lastDigit = 0
result = 0
for line in Lines:
    gotFirst = False
    ### Part 2
    line = replaceWrittenNumbers(line)
    ###
    for char in line:
        if char.isnumeric():
            if not gotFirst:
                firstDigit = char
                gotFirst = True
            lastDigit = char
    result += int(firstDigit+lastDigit)

print(result)