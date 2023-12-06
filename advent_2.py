
######### MAIN #######

file1 = open(r'C:\WorkSpace\aoc2023\input2.txt', 'r')
Lines = file1.readlines()
result = 0
for line in Lines:
    game = int(line.split(':')[0].split(' ')[1])
    gameNotFine = False
    for set in line.split(':')[1].split(';'):
        for take in set.strip().split(','):
            print(take.strip())
            if take.strip().split(' ')[1] == "red" and int(take.strip().split(' ')[0]) > 12:
                  print(f"{take.strip().split(' ')[0]} > 12")
                  gameNotFine = True
            if take.strip().split(' ')[1] == "green" and int(take.strip().split(' ')[0]) > 13:
                  print(f"{take.strip().split(' ')[0]} > 13")
                  gameNotFine = True
            if take.strip().split(' ')[1] == "blue" and int(take.strip().split(' ')[0]) > 14:
                  print(f"{take.strip().split(' ')[0]} > 14")
                  gameNotFine = True        
    if not gameNotFine:
        print(f"######### game {game} is fine)")
        result += game
print(result)