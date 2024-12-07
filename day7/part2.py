from collections import defaultdict

file = open("day6/input.txt","r")

found = set()

curr = ()
area = []
cnt = 0
for line in file.readlines():
    line = line.rstrip()

    area.append(list(line))

    if '^' in line:
        curr = (cnt, line.index('^'))

    cnt += 1


direction = 0
diffs = [(-1, 0), (0, 1), (1, 0), (0, -1)] 


def simulate(block):

    found = set()

    local_curr = curr

    local_direction = direction
    
    while 0 <= local_curr[0] < len(area) and 0 <= local_curr[1] < len(area[0]):

        state = (local_curr, local_direction)

        if state in found:
            return True  
        
        found.add(state)
        
  
        next_curr = (local_curr[0] + diffs[local_direction][0], local_curr[1] + diffs[local_direction][1])
        

        if (next_curr == block) or (0 <= next_curr[0] < len(area) and 0 <= next_curr[1] < len(area[0]) and area[next_curr[0]][next_curr[1]] == '#'):
            local_direction = (local_direction + 1) % 4
        else:
            local_curr = next_curr
    
    return False 

found_loops = set()

for i in range(len(area)):
    for j in range(len(area[0])):
        if area[i][j] != '#' and (i, j) != curr:
            if simulate((i, j)):
                found_loops.add((i, j))

print(len(found_loops))
