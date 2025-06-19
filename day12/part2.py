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
        sides = {}
        sides_fake = set()
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
                    key = "UP" + str(curr_row)
                    if key not in sides:
                        sides[key] = [curr]
                    else:
                        encountered = False
                        for rep_row, rep_col in sides[key]:
                            step = 1 if curr_col > rep_col else -1
                            clear_path = True

                            for i in range(rep_col + step, curr_col, step):
                                if garden[curr_row][i] != garden[curr_row][curr_col]:
                                    clear_path = False
                                    break
                                if garden[curr_row - 1][i] == garden[curr_row][curr_col]:
                                    clear_path = False
                                    break
                               

                            if clear_path:
                                encountered = True
                                break

                        if not encountered:
                            sides[key].append(curr)
                else:
                    stack.append((curr_row - 1, curr_col))
            else:
                key = "UP" + str(curr_row)
                if key not in sides:
                    sides[key] = [curr]
                else:
                    encountered = False
                    for rep_row, rep_col in sides[key]:
                        step = 1 if curr_col > rep_col else -1
                        clear_path = True

                        for i in range(rep_col + step, curr_col, step):
                            if garden[curr_row][i] != garden[curr_row][curr_col]:
                                clear_path = False
                                break
                            

                        if clear_path:
                            encountered = True
                            break

                    if not encountered:
                        sides[key].append(curr)

            if curr_row != len(garden) - 1:
                if garden[curr_row + 1][curr_col] != garden[curr_row][curr_col]:
                    key = "DOWN" + str(curr_row)
                    if key not in sides:
                        sides[key] = [curr]
                    else:
                        encountered = False
                        for rep_row, rep_col in sides[key]:
                            step = 1 if curr_col > rep_col else -1
                            clear_path = True

                            for i in range(rep_col + step, curr_col, step):
                                if garden[curr_row][i] != garden[curr_row][curr_col]:
                                    clear_path = False
                                    break
                                if curr_row + 1 < len(garden) and garden[curr_row + 1][i] == garden[curr_row][curr_col]:
                                    clear_path = False
                                    break

                            if clear_path:
                                encountered = True
                                break

                        if not encountered:
                            sides[key].append(curr)
                else:
                    stack.append((curr_row + 1, curr_col))
            else:
                key = "DOWN" + str(curr_row)
                if key not in sides:
                    sides[key] = [curr]
                else:
                    encountered = False
                    for rep_row, rep_col in sides[key]:
                        step = 1 if curr_col > rep_col else -1
                        clear_path = True

                        for i in range(rep_col + step, curr_col, step):
                            if garden[curr_row][i] != garden[curr_row][curr_col]:
                                clear_path = False
                                break

                        if clear_path:
                            encountered = True
                            break

                    if not encountered:
                        sides[key].append(curr)
            
            if curr_col != 0:
                if garden[curr_row][curr_col-1] != garden[curr_row][curr_col]:
                    key = "LEFT" + str(curr_col)
                    if key not in sides:
                        sides[key] = [curr]
                    else:
                        encountered = False
                        for rep_row, rep_col in sides[key]:
                            step = 1 if curr_row > rep_row else -1
                            clear_path = True

                            for i in range(rep_row + step, curr_row, step):
                                if garden[i][curr_col] != garden[curr_row][curr_col]:
                                    clear_path = False
                                    break
                                if garden[i][curr_col - 1] == garden[curr_row][curr_col]:
                                    clear_path = False
                                    break
                               

                            if clear_path:
                                encountered = True
                                break

                        if not encountered:
                            sides[key].append(curr)
                else:
                    stack.append((curr_row, curr_col-1))
            else:
                key = "LEFT" + str(curr_col)
                if key not in sides:
                    sides[key] = [curr]
                else:
                    encountered = False
                    for rep_row, rep_col in sides[key]:
                        step = 1 if curr_row > rep_row else -1
                        clear_path = True

                        for i in range(rep_row + step, curr_row, step):
                            if garden[i][curr_col] != garden[curr_row][curr_col]:
                                clear_path = False
                                break

                        if clear_path:
                            encountered = True
                            break

                    if not encountered:
                        sides[key].append(curr)

            if curr_col != len(garden[0]) - 1:
                if garden[curr_row ][curr_col+1] != garden[curr_row][curr_col]:
                    key = "RIGHT" + str(curr_col)
                    if key not in sides:
                        sides[key] = [curr]
                    else:
                        encountered = False
                        for rep_row, rep_col in sides[key]:
                            step = 1 if curr_row > rep_row else -1
                            clear_path = True

                            for i in range(rep_row + step, curr_row, step):
                                if garden[i][curr_col] != garden[curr_row][curr_col]:
                                    clear_path = False
                                    break
                                if garden[i][curr_col + 1] == garden[curr_row][curr_col]:
                                    clear_path = False
                                    break
                               

                            if clear_path:
                                encountered = True
                                break

                        if not encountered:
                            sides[key].append(curr)
                else:
                    stack.append((curr_row , curr_col+1))
            else:
                key = "RIGHT" + str(curr_col)
                if key not in sides:
                    sides[key] = [curr]
                else:
                    encountered = False
                    for rep_row, rep_col in sides[key]:
                        step = 1 if curr_row > rep_row else -1
                        clear_path = True

                        for i in range(rep_row + step, curr_row, step):
                            if garden[i][curr_col] != garden[curr_row][curr_col]:
                                clear_path = False
                                break
                            

                        if clear_path:
                            encountered = True
                            break

                    if not encountered:
                        sides[key].append(curr)
        
  
        sides_sum = 0

        for case in sides:
            sides_sum += len(sides[case])

        total += area * sides_sum

print(total)

            