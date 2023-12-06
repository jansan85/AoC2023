def getNumberFromNumberPosition(line, position):
    #print(f"getNumberFromNumberPosition: {position}")
    if position == 0:
        startPos = position
    elif line[position:position+1].isnumeric():
        startPos = position
        if line[position-1:position].isnumeric():
            startPos = position-1
            if position == 1:
                print("stelle 1 stinkt")
            elif line[position-2:position-1].isnumeric():
                startPos = position-2
    #else:
    #    print("requested Number is not there!!!")
    #    return 0
    #print(f"getNumberFromNumberPosition StartPosition: {startPos}")
    number = str(line[startPos])
    #print(f"first: {line[startPos]}")
    if line[startPos+1:startPos+2].isnumeric():
        number = number + str(line[startPos+1])
        #print(f"second: {line[startPos+1]}")
        if line[startPos+2:startPos+3].isnumeric():
            number = number + str(line[startPos+2])
            #print(f"third: {line[startPos+2]}")
    print(number)
    return number


    
    

file1 = open(r'C:\WorkSpace\aoc2023\input3.txt', 'r')
Lines = file1.readlines()

result = 0

engine = []
for line in Lines:
    engine.append(line.strip())

#print(engine[0][6:1])

lineCount = 0
for line in engine:
    print(f"############# Zeile {lineCount} #############################################################")
    charPos = 0
    for char in line:
        if not char.isnumeric() and not char == "." :
            print(char)
            #print(engine[lineCount][charPos:charPos+1])
            #check rechts:
            if not charPos == 140 and engine[lineCount][charPos+1:charPos+2].isnumeric():
                print("rechts!")
                result += int(getNumberFromNumberPosition((engine[lineCount]),(charPos+1)))
            #check links:
            if not charPos == 0 and engine[lineCount][charPos-1:charPos].isnumeric():
                print("links!")
                result += int(getNumberFromNumberPosition((engine[lineCount]),(charPos-1)))
            #check drüber:
            if lineCount > 0:
                diag = True
                if engine[lineCount-1][charPos:charPos+1].isnumeric():
                    print("drüber!")
                    result += int(getNumberFromNumberPosition((engine[lineCount-1]),(charPos)))
                    diag = False
                if diag and engine[lineCount-1][charPos-1:charPos].isnumeric():
                    print("diag drüber links!")
                    result += int(getNumberFromNumberPosition((engine[lineCount-1]),(charPos-1)))
                if diag and engine[lineCount-1][charPos+1:charPos+2].isnumeric():
                    print("diag drüber rechts!")
                    result += int(getNumberFromNumberPosition((engine[lineCount-1]),(charPos+1)))
            #check drunter
            if lineCount < 141:
                diag = True
                if engine[lineCount+1][charPos:charPos+1].isnumeric():
                    print("drunter!")
                    result += int(getNumberFromNumberPosition((engine[lineCount+1]),(charPos)))
                    diag = False
                if diag and engine[lineCount+1][charPos-1:charPos].isnumeric():
                    print("diag drunter links!")
                    result += int(getNumberFromNumberPosition((engine[lineCount+1]),(charPos-1)))
                if diag and engine[lineCount+1][charPos+1:charPos+2].isnumeric():
                    print("diag drunter rechts!")
                    result += int(getNumberFromNumberPosition((engine[lineCount+1]),(charPos+1)))
        charPos += 1
    lineCount += 1
print(result)