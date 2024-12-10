from collections import defaultdict
from math import gcd
from collections import deque


file = open("day10/input.txt","r")



matrix = []


for line in file.readlines():
    line = line.rstrip()
    

    matrix.append([int(i) for i in list(line)])


total = 0


def search(start):
    queue = deque()


    queue.append(start)


    found_peaks = 0

    visited = set()


    while queue:
        
        curr = queue.popleft()

        visited.add(curr)

        if matrix[curr[0]][curr[1]] == 9:
            found_peaks += 1
        else:
            deltas = [(-1,0), (1,0), (0,-1), (0,1)]

            for delta in deltas:
                dx = delta[0]
                dy = delta[1]

                new_y = curr[0] + dy
                new_x = curr[1] + dx

                if 0 <= new_x < len(matrix[0]) and 0 <= new_y < len(matrix):
                    if matrix[curr[0]][curr[1]] + 1 == matrix[new_y][new_x]:
                        queue.append((new_y,new_x))


    
    return found_peaks



for row in range(len(matrix)):
    for col in range(len(matrix[1])):
        if matrix[row][col] == 0:
            score = search((row,col))

            total += score


print(total)
