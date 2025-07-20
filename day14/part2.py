import os
from PIL import Image, ImageDraw

file = open("day14/input.txt","r")
robots = []

WIDTH = 101
HEIGHT = 103

# Parse input
for line in file.readlines():
    line = line.rstrip().split(" ")
    pos = list(map(int, line[0][2:].split(",")))
    v = list(map(int, line[1][2:].split(",")))
    robots.append((pos, v))

# Output folder
output_folder = "frames"
os.makedirs(output_folder, exist_ok=True)

for second in range(10000):
    grid = [[' ' for _ in range(WIDTH)] for _ in range(HEIGHT)]
    positions = {}
    repeat = False

    for pos, v in robots:
        x = (pos[0] + v[0] * second) % WIDTH
        y = (pos[1] + v[1] * second) % HEIGHT

    
        positions[(x, y)] = True
        grid[y][x] = '*'

    for row in grid:
        if '*' * 5 in ''.join(row):
            img = Image.new("RGB", (WIDTH, HEIGHT), "black")
            draw = ImageDraw.Draw(img)

            for y in range(HEIGHT):
                for x in range(WIDTH):
                    if grid[y][x] == '*':
                        draw.point((x, y), fill="white")

   
   

            img.save(os.path.join(output_folder, f"frame_{second:03d}.png"))
