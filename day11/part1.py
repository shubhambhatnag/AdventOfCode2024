import math

file = open("day11/input.txt","r")

# def length(num):
#     return math.floor(math.log10(abs(num))) + 1 if num != 0 else 1
from collections import defaultdict

def blink(state):

    def count_digits(n):
        return len(str(abs(n)))

    new_state = defaultdict(int)

    for value, count in state.items():
        if value == 0:
            new_state[1] += count
        elif count_digits(value) % 2 == 0:
            str_num = str(value)
            
            left = int(str_num[:(len(str_num) // 2)])
            right = int(str_num[(len(str_num) // 2):])

            new_state[left] += count
            new_state[right] += count
        else:
            new_state[value * 2024] += count
        
    return new_state

    


stones = []

for line in file.readlines():
    line = line.rstrip()

    stones = [int(i) for i in line.split(" ")]



    


state = {stone: stones.count(stone) for stone in set(stones)}

for i in range(25):
    state = blink(state)

print(sum(state.values()))
    
