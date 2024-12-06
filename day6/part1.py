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

diffs = [(-1,0), (0,1), (1,0), (0,-1)]

while 0 <= curr[0] < len(area) and 0 <= curr[1] < len(area[0]):
    pos = area[curr[0]][curr[1]]


    if pos == '#':
        curr = (curr[0] - diffs[direction % 4][0], curr[1] - diffs[direction % 4][1])

        direction += 1
    
    else:

        found.add(curr)

        curr = (curr[0] + diffs[direction % 4][0], curr[1] + diffs[direction % 4][1])


print(len(found))





