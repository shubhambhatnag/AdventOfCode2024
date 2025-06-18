import math

file = open("day12/input.txt","r")

garden = []
for line in file.readlines():
    line = line.rstrip()

    garden.append(list(line))


found = set()

total = 0

for row in range(len(garden)):
    for col in range(len(garden)):
        if (row,col) in found:
            continue

        area = 0
        sides = set()

        stack = [(row,col)]

        while stack != []:
            curr = stack.pop()
            curr_row, curr_col = curr
            if curr in found:
                continue

            area += 1

            found.add(curr)

            if curr_row != 0:
                if garden[curr_row - 1][curr_col] != garden[curr_row][curr_col]:
                    sides.add("above"+str(curr_row))
                else:
                    stack.append((curr_row - 1, curr_col))
            else:
                sides.add("above"+str(curr_row))

            if curr_row != len(garden) - 1:
                if garden[curr_row + 1][curr_col] != garden[curr_row][curr_col]:
                    sides.add("below"+str(curr_row))
                else:
                    stack.append((curr_row + 1, curr_col))
            else:
                sides.add("below"+str(curr_row))
            
            if curr_col != 0:
                if garden[curr_row][curr_col-1] != garden[curr_row][curr_col]:
                    sides.add("left"+str(curr_col))
                else:
                    stack.append((curr_row, curr_col-1))
            else:
                sides.add("left"+str(curr_col))

            if curr_col != len(garden[0]) - 1:
                if garden[curr_row ][curr_col+1] != garden[curr_row][curr_col]:
                    sides.add("right"+str(curr_col))
                else:
                    stack.append((curr_row , curr_col+1))
            else:
                sides.add("right"+str(curr_col))
        
        # print(area, perimeter)

        print(garden[row][col], sides)
        total += area * len(sides)

print(total)

            

            







