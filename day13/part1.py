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
        prize[i] = int(prize[i].strip()[2:])



    cost = None

    curr = [0,0]

    for i in range(101):
        new_prize = [prize[0] - B[0] * i, prize[1] - B[1] * i]

        if new_prize[0] % A[0] == 0 and new_prize[1] % A[1] == 0 and new_prize[0]/A[0] == new_prize[1]/A[1]:
            if cost == None:
                cost = i + 3 * new_prize[0] // A[0]
            else:
                cost = min(cost, i + 3 * new_prize[0] //A[0])

    if cost != None:
        total += cost   


print(total)


