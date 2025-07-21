file = open("day15/input.txt","r")


factory = []
moves = []
matrix_check = True


for line in file.readlines():
    line = line.rstrip()
    if line == "":
        matrix_check = False
    if matrix_check:
        factory.append(list(line))
    else:
        moves.extend(list(line))


for row in range(len(factory)):
    if "@" in factory[row]:
        robot_pos = [row, factory[row].index("@")]




for move in moves:
    if move == ">":
        x_pos = robot_pos[1]
        
        while x_pos <= len(factory):
            
            if factory[robot_pos[0]][x_pos + 1] == '#':
                break
            elif factory[robot_pos[0]][x_pos + 1] == '.':
                factory[robot_pos[0]][robot_pos[1]:x_pos+2] = ['.'] + factory[robot_pos[0]][robot_pos[1]:x_pos+1]
                robot_pos[1] += 1
                break
            else:
                x_pos += 1

    if move == "<":
        x_pos = robot_pos[1]
        
        while x_pos >= 0:
            
            if factory[robot_pos[0]][x_pos - 1] == '#':
                break
            elif factory[robot_pos[0]][x_pos - 1] == '.':
                factory[robot_pos[0]][x_pos-1:robot_pos[1]+1] = factory[robot_pos[0]][x_pos:robot_pos[1]+1] + ['.']
                robot_pos[1] -= 1
                break
            else:
                x_pos -= 1
    
    if move == "^":
        y_pos = robot_pos[0]
       
        while y_pos >= 0:
            if factory[y_pos - 1][robot_pos[1]] == '#':
                break
            elif factory[y_pos - 1][robot_pos[1]] == '.':
                for i in range(y_pos - 1, robot_pos[0]):
                    factory[i][robot_pos[1]] = factory[i + 1][robot_pos[1]]
                factory[robot_pos[0]][robot_pos[1]] = '.'
                robot_pos[0] -= 1
                break
            else:
                y_pos -= 1
                
    if move == "v":
        y_pos = robot_pos[0]
       
        while y_pos < len(factory) - 1:
            if factory[y_pos + 1][robot_pos[1]] == '#':
                break
            elif factory[y_pos + 1][robot_pos[1]] == '.':
                for i in range(y_pos + 1, robot_pos[0], -1):
                    factory[i][robot_pos[1]] = factory[i - 1][robot_pos[1]]
                factory[robot_pos[0]][robot_pos[1]] = '.'
                robot_pos[0] += 1
                break
            else:
                y_pos += 1


total = 0


for row in range(len(factory)):
    for col in range(len(factory[0])):
        if factory[row][col] == 'O':
            gps = 100 * row + col
            total += gps


print(total)


