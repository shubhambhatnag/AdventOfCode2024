file = open("day15/input.txt","r")


factory = []
moves = []
matrix_check = True


for line in file.readlines():
    line = line.rstrip()
    if line == "":
        matrix_check = False
    if matrix_check:
        new_line = []
        for ch in line:
            if ch == '#':
                new_line.extend('##')
            elif ch == 'O':
                new_line.extend('[]')
            elif ch == '.':
                new_line.extend('..')
            elif ch == '@':
                new_line.extend('@.')
        

        factory.append(new_line)
    else:
        moves.extend(list(line))


for row in range(len(factory)):
    if "@" in factory[row]:
        robot_pos = [row, factory[row].index("@")]



        
# print("TEST: ", can_move_up(robot_pos[0], robot_pos[1], False))

# I know this is a really stupid way of making it but if it works it works amirite
def move_up(row, col, side_check):
    if not (0 <= row < len(factory)) or not (0 <= col < len(factory[0])):
        return

    if factory[row][col] == ".":
        return

    if factory[row][col] == "@":
        if row - 1 >= 0:
            move_up(row - 1, col, False)
            factory[row - 1][col] = "@"
            factory[row][col] = "."
    elif factory[row][col] == "[":
        if side_check:
            if row - 1 >= 0:
                move_up(row - 1, col, False)
                factory[row - 1][col] = "["
                factory[row][col] = "."
        else:
            if col + 1 < len(factory[0]):
                move_up(row, col + 1, True)
            if row - 1 >= 0:
                move_up(row - 1, col, False)
                factory[row - 1][col] = "["
                factory[row][col] = "."
    elif factory[row][col] == "]":
        if side_check:
            if row - 1 >= 0:
                move_up(row - 1, col, False)
                factory[row - 1][col] = "]"
                factory[row][col] = "."
        else:
            if col - 1 >= 0:
                move_up(row, col - 1, True)
            if row - 1 >= 0:
                move_up(row - 1, col, False)
                factory[row - 1][col] = "]"
                factory[row][col] = "."
    else:
        print(f"somethings gone wrong: {factory[row][col]} at ({row},{col})")


def move_down(row, col, side_check):
    if not (0 <= row < len(factory)) or not (0 <= col < len(factory[0])):
        return

    if factory[row][col] == ".":
        return

    if factory[row][col] == "@":
        if row + 1 < len(factory):
            move_down(row + 1, col, False)
            factory[row + 1][col] = "@"
            factory[row][col] = "."
    elif factory[row][col] == "[":
        if side_check:
            if row + 1 < len(factory):
                move_down(row + 1, col, False)
                factory[row + 1][col] = "["
                factory[row][col] = "."
        else:
            if col + 1 < len(factory[0]):
                move_down(row, col + 1, True)
            if row + 1 < len(factory):
                move_down(row + 1, col, False)
                factory[row + 1][col] = "["
                factory[row][col] = "."
    elif factory[row][col] == "]":
        if side_check:
            if row + 1 < len(factory):
                move_down(row + 1, col, False)
                factory[row + 1][col] = "]"
                factory[row][col] = "."
        else:
            if col - 1 >= 0:
                move_down(row, col - 1, True)
            if row + 1 < len(factory):
                move_down(row + 1, col, False)
                factory[row + 1][col] = "]"
                factory[row][col] = "."
    else:
        print(f"somethings gone wrong: {factory[row][col]} at ({row},{col})")

    
def can_move_vertical(row, col, direction):
    
    if factory[row][col] == "#":
        return False
    
    if factory[row][col] == ".":
        return True
    
    next_row = row + direction
    
    if not (0 <= next_row < len(factory)):
        return False
    
    if factory[row][col] == "@":
        return can_move_vertical(next_row, col, direction)
    elif factory[row][col] == "[":
        return (can_move_vertical(next_row, col, direction) and can_move_vertical(next_row, col + 1, direction))
    elif factory[row][col] == "]":
        return (can_move_vertical(next_row, col, direction) and can_move_vertical(next_row, col - 1, direction))


for move in moves:
    
    if move == ">":
        x_pos = robot_pos[1]
        
        while x_pos <= len(factory[0]):
            
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

        if can_move_vertical(robot_pos[0], robot_pos[1], -1):
            move_up(robot_pos[0],robot_pos[1], False)
            robot_pos[0] -= 1
       

                
    if move == "v":
        if can_move_vertical(robot_pos[0], robot_pos[1], 1):
            move_down(robot_pos[0],robot_pos[1], False)
            robot_pos[0] += 1

    # print("moving", move)
    # for row in factory:
    #     print("".join(row))

total = 0



for row in range(len(factory)):
    for col in range(len(factory[0])):
        if factory[row][col] == '[':
            gps = 100 * row + col
            total += gps


print(total)


