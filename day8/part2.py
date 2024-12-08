from collections import defaultdict
from math import gcd

file = open("day8/input.txt","r")

antinodes = set()

matrix = []
for line in file.readlines():
    line = line.rstrip()
    
    matrix.append(list(line))



for row in range(len(matrix)):
    for col in range(len(matrix[0])):

        dist_dict = defaultdict(list)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                

                if matrix[i][j] != ".":
                    distance = abs(i - row) + abs(j - col)
                    slopex = i - row
                    slopey = j - col

                    g = gcd(slopex,slopey)

                    if g == 0:
                        slope = (None,None)
                    else:
                        slope = (slopex/g, slopey/g)
                    
                    dist_dict[matrix[i][j]].append((distance, slope))


        for letter in dist_dict: 

            if len(dist_dict[letter]) >= 2 and matrix[row][col] == letter:
                antinodes.add((row, col))
            slopes = defaultdict(int)

            for _, slope in dist_dict[letter]:
                slopes[slope] += 1

            for slope in slopes:
                if slopes[slope] > 1:
                    antinodes.add((row, col))
                    break

print(len(antinodes))
        


