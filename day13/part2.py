import numpy as np

file = open("day13/input.txt","r")

total = 0

lines = file.readlines()

lines.append("")

machines = [lines[i:i+4] for i in range(0, len(lines), 4)]

for machine in machines:
    A = machine[0].rstrip().split(':')[1].split(",")
    for i in range(len(A)):
        A[i] = int(A[i][2:])


    B = machine[1].rstrip().split(':')[1].split(",")
    for i in range(len(B)):
        B[i] = int(B[i][2:])

  
    
    prize = machine[2].rstrip().lstrip().split(':')[1].split(",")
    for i in range(len(prize)):
        prize[i] = int(prize[i].strip()[2:]) + 10000000000000


    A = list(map(float, A))
    B = list(map(float, B))
    prize = list(map(float, prize))


    cost = None

    # eq1 - A[0] * a + B[0] * b = prize[0]
    # eq2 - A[1] * a + B[1] * b = prize[1]

    det = A[0] * B[1] - A[1] * B[0]

    if det != 0:
        det_a = prize[0] * B[1] - prize[1] * B[0]
        det_b = A[0] * prize[1] - A[1] * prize[0]

        
        a = det_a / det
        b = det_b / det

        if a.is_integer() and b.is_integer():
            total += int(a)*3 + int(b)

   

print(total)


