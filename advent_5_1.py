def changeValueForLine(i:int, line):
    #print(f"i = {i} >= {line.split()[1]} | <= {line.split()[1]} + {line.split()[2]} >>>> {(int(line.split()[1]) + int(line.split()[2]))}")
    if int(i) >= int(line.split()[1]) and int(i) <= int(int(line.split()[1]) + int(line.split()[2])):
        return (int(i) + (int(line.split()[0]) - int(line.split()[1])))
    return int(i)


#################################### MAIN #################

file1 = open(r'C:\WorkSpace\aoc2023\input5.txt', 'r')
Lines = file1.readlines()
result = []

for count,line in enumerate(Lines):
    if count == 0:
        seeds = (line.strip().split(':')[1].strip().split(' '))

for seed in seeds:
    print(f"# # # # # Seed: {seed}")       
    for count,line in enumerate(Lines):
        if line.strip().endswith(':'):
            changed = False
        if line.strip().split(' ')[0].isnumeric():
            if int(seed) >= int(line.strip().split()[1]) and int(seed) <= int(int(line.strip().split()[1]) + int(line.strip().split()[2])) and not changed:
                seed = (int(seed) + (int(line.strip().split()[0]) - int(line.strip().split()[1])))
                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                changed = True
            print(line.strip())      
            #seed = changeValueForLine(seed, line.strip())
            print(f"New: {seed}")
        else:
            print(line.strip().split(' ')[0])
    result.append(seed)
print(f"RESULT: {min(result)}")


