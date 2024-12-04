import re
file = open("day3/input.txt","r")

total = 0
for line in file.readlines():
    line = line.rstrip()
    curr = 0

    pattern = r"mul\((\d{1,}),(\d{1,})\)"

    matches = re.findall(pattern, line)

    for e1,e2 in matches:
        total += int(e1) * int(e2)
    

print(total)



        





    