
######### MAIN #######

file1 = open(r'C:\WorkSpace\aoc2023\input2.txt', 'r')
Lines = file1.readlines()
result = 0
for line in Lines:
    game = int(line.split(':')[0].split(' ')[1])
    gameNotFine = False
    red = 0
    green = 0
    blue = 0
    for set in line.split(':')[1].split(';'):
        for take in set.strip().split(','):
            print(take.strip())
            if take.strip().split(' ')[1] == "red" and int(take.strip().split(' ')[0]) > red:
                  red = int(take.strip().split(' ')[0])
            if take.strip().split(' ')[1] == "green" and int(take.strip().split(' ')[0]) > green:
                  green = int(take.strip().split(' ')[0])
            if take.strip().split(' ')[1] == "blue" and int(take.strip().split(' ')[0]) > blue:
                 blue = int(take.strip().split(' ')[0])
    print(f"{red} * {green} * {blue}")
    result += (red * green * blue)
print(result)