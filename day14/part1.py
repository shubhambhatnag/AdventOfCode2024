file = open("day14/input.txt","r")
quadrants = [0,0,0,0]

WIDTH = 101
HEIGHT = 103

for line in file.readlines():
    line = line.rstrip().split(" ")
    pos = list(map(int, line[0][2:].split(",")))
    v = list(map(int, line[1][2:].split(",")))
    
    pos[0] = (pos[0] + (v[0] * 100)) % WIDTH
    pos[1] = (pos[1] + (v[1] * 100)) % HEIGHT
    
    if pos[0] == WIDTH // 2 or pos[1] == HEIGHT // 2:
        continue
    

    if pos[0] > WIDTH // 2 and pos[1] > HEIGHT // 2:
        quadrants[0] += 1 
    elif pos[0] < WIDTH // 2 and pos[1] > HEIGHT // 2:
        quadrants[1] += 1 
    elif pos[0] < WIDTH // 2 and pos[1] < HEIGHT // 2:
        quadrants[2] += 1 
    elif pos[0] > WIDTH // 2 and pos[1] < HEIGHT // 2:
        quadrants[3] += 1 


factor = 1
for quadrant in quadrants:
    factor *= quadrant
print(factor)