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
        perimeter = 0

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
                    perimeter += 1
                else:
                    stack.append((curr_row - 1, curr_col))
            else:
                perimeter += 1

            if curr_row != len(garden) - 1:
                if garden[curr_row + 1][curr_col] != garden[curr_row][curr_col]:
                    perimeter += 1
                else:
                    stack.append((curr_row + 1, curr_col))
            else:
                perimeter += 1
            
            if curr_col != 0:
                if garden[curr_row][curr_col-1] != garden[curr_row][curr_col]:
                    perimeter += 1
                else:
                    stack.append((curr_row, curr_col-1))
            else:
                perimeter += 1

            if curr_col != len(garden[0]) - 1:
                if garden[curr_row ][curr_col+1] != garden[curr_row][curr_col]:
                    perimeter += 1
                else:
                    stack.append((curr_row , curr_col+1))
            else:
                perimeter += 1
        
        # print(area, perimeter)
        total += area * perimeter

print(total)

            

            







