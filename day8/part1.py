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
                if i == row and j == col:
                    continue

                if matrix[i][j] != ".":
                    distance = abs(i - row) + abs(j - col)
                    slopex = i - row
                    slopey = j - col

                    g = gcd(slopex,slopey)
                    slope = (slopex/g, slopey/g)
                    dist_dict[matrix[i][j]].append((distance, slope))


        for letter in dist_dict: 

            slopes = defaultdict(list)

            for distance, slope in dist_dict[letter]:
                slopes[slope].append(distance)

            for slope in slopes:
                distances = sorted(slopes[slope])
                for i in range(len(distances) - 1):
                    if distances[i] * 2 == distances[i + 1]:
                        antinodes.add((row, col))
                        break

print(len(antinodes))
        






