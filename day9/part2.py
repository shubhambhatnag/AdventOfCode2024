from collections import defaultdict
from math import gcd

file = open("day9/input.txt","r")



disk = []

total_data = 0

block_size = {}


for line in file.readlines():
    line = line.rstrip()
    

    curr_id = 0
    for pos in range(len(line)):
        if pos % 2 == 0:
            disk += [curr_id] * int(line[pos])
            total_data += int(line[pos])
            block_size[curr_id] = int(line[pos])
            curr_id += 1
        else:
            disk += ["."] * int(line[pos])



free = 0

rightmost = len(disk) - 1


while rightmost >= 0:
    print(rightmost)
    while disk[rightmost] == '.':
        rightmost -= 1
    
    block_length = block_size[disk[rightmost]]

    curr = 0

    while curr < len(disk) - block_length + 1 and curr < rightmost:
        if set(disk[curr:curr+block_length]) == {'.'}:
            disk[curr:curr+block_length] = [disk[rightmost]] * block_length
            disk[rightmost - block_length + 1:rightmost+1] = ['.'] * block_length
            break
        curr += 1
    
    rightmost -= 1



checksum = 0

for i in range(len(disk)):
    if disk[i] == '.':
        continue
    checksum += disk[i] * i


print(checksum)
