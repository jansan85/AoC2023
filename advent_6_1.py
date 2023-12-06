def calcPossibleDistances(time):
    speed = 0
    possibleDistances = []
    while int(time) >= 0:
        possibleDistances.append(int(time) * speed)
        time = int(time) - 1
        speed += 1
    return possibleDistances


file1 = open(r'C:\WorkSpace\aoc2023\input6.txt', 'r')
Lines = file1.readlines()

times = []
recordDistances = []
result = 1

for count, line in enumerate(Lines):
    if count == 0:
        times = line.strip().split(":")[1].strip().split()
    if count == 1:
        recordDistances = line.strip().split(":")[1].strip().split()

for race, time in enumerate(times):
    racesWon = 0
    #print(f"time: {time} distance: {recordDistances[race]}")
    possibleDistances = calcPossibleDistances(time)
    for r in possibleDistances:
        if int(r) > int(recordDistances[race]):
            racesWon += 1
    #print(f"In race {race} races Won {racesWon}")
    result *= racesWon

print(result)