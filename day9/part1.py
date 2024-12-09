from collections import defaultdict
from math import gcd

file = open("day9/input.txt","r")



disk = []

total_data = 0

for line in file.readlines():
    line = line.rstrip()
    

    curr_id = 0
    for pos in range(len(line)):
        if pos % 2 == 0:
            disk += [curr_id] * int(line[pos])
            total_data += int(line[pos])
            curr_id += 1
        else:
            disk += ["."] * int(line[pos])



free = 0

rightmost = len(disk) - 1

while set(disk[total_data:]) != {'.'}:
    while disk[free] != '.':
        free += 1
    
    while disk[rightmost] == '.':
        rightmost -= 1

    disk[free], disk[rightmost] = disk[rightmost], disk[free]


checksum = 0

for i in range(len(disk)):
    if disk[i] == '.':
        continue
    checksum += disk[i] * i


print(checksum)
