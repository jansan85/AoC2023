def getHandValue(hand):
    value = str()
    for i in hand:
        if i.split(",")[0] == "2":
            value = value + "02"
        elif i.split(",")[0] == "3":
            value = value + "03"
        elif i.split(",")[0] == "4":
            value = value + "04"
        elif i.split(",")[0] == "5":
            value = value + "05"
        elif i.split(",")[0] == "6":
            value = value + "06"
        elif i.split(",")[0] == "7":
            value = value + "07"
        elif i.split(",")[0] == "8":
            value = value + "08"
        elif i.split(",")[0] == "9":
            value = value + "09"
        elif i.split(",")[0] == "T":
            value = value + "10"
        elif i.split(",")[0] == "J":
            value = value + "11"
        elif i.split(",")[0] == "Q":
            value = value + "12"
        elif i.split(",")[0] == "K":
            value = value + "13"
        elif i.split(",")[0] == "A":
            value = value + "14"
    return value



def calcValueForHandresult(handResult):
    print(f"calculating handresult for {handResult}")
    for count, i in enumerate(handResult):
        if i.split(",")[0] == "5":
            return 500
        elif i.split(",")[0] == "4":
            return 400
        elif i.split(",")[0].split(",")[0] == "3":
            if handResult[count+1].split(",")[0] == "2":
                return 350
            else:
                return 300
        elif i.split(",")[0] == "2":
            if handResult[count+1].split(",")[0] == "2":
                return 250
            else:
                return 200
        else:
            return 100
        print(i.split(",")[0])
        


###### MAIN #######

file1 = open(r'C:\WorkSpace\aoc2023\input7.txt', 'r')
Lines = file1.readlines()

resultList = []
for line in Lines:
    hand = line.strip().split()[0]
    playedCard = []
    print(hand)
    handValue = getHandValue(hand)
    handResult = []
    for card in hand:
        cardResult = []
        if card not in playedCard:
            cardResult.append
            handResult.append((str(hand.count(card)) + "," + card))
            #print(f"{card} in {hand} = {hand.count(card)}")
            playedCard.append(card)
    handResult = sorted(handResult, reverse=True)
    #print(handResult)
    value = calcValueForHandresult(handResult)
    print(f"value: {value}")
    gameItem = []
    gameItem.append(str(value))
    gameItem.append(hand)
    gameItem.append(line.strip().split()[1])
    gameItem.append(handValue)

    #gameItem = (str(value) + ";" + hand + ";" + line.strip().split()[1])
    print(gameItem)
    resultList.append(gameItem)

print("###########################")
#resultList = (sorted(resultList))
resultList = sorted(resultList, key=lambda x:(x[0], x[3]))

print(resultList)
#print(x_resultList)

finalResult = 0
for count, result in enumerate(resultList):
    print(f"{count} | {result[0]} | {result[1]} | {result[3]}")
    finalResult += (count+1) * int(result[2])

print(finalResult)