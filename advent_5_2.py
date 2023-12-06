
#################################### MAIN #################

file1 = open(r'C:\WorkSpace\aoc2023\input5_2.txt', 'r')
Lines = file1.readlines()
result = []

#part 1
for count,line in enumerate(Lines):
    if count == 0:
        seeds = (line.strip().split(':')[1].strip().split(' '))

#part 2
i = 111184803
k = 2169258488
while i>1:
    seeds.append(k)
    k += 10000
    i -= 10000
    

# for every seed
for seed in seeds:     
    for count,line in enumerate(Lines):
        #identify new bunch of maps
        if line.strip().endswith(':'):
            changed = False
        if line.strip().split(' ')[0].isnumeric():
            # if in range add src-dest to seed
            if int(seed) >= int(line.strip().split()[1]) and int(seed) <= int(int(line.strip().split()[1]) + int(line.strip().split()[2])) and not changed:
                seed = (int(seed) + (int(line.strip().split()[0]) - int(line.strip().split()[1])))
                changed = True
    result.append(seed)
print(f"RESULT: {min(result)}")


