file = open("day2/input.txt","r")

safe = 0

def check_valid(line):

    increasing = None

    valid = True

    for i in range(len(line) - 1):
        if line[i] < line[i+1]:
            if increasing == None:
                increasing = True
            elif increasing == False:
                valid = False
                break

            if not ((line[i+1] - line[i]) >= 1 and (line[i+1] - line[i]) <= 3):
                valid = False
                break


        else:
            if increasing == None:
                increasing = False
            elif increasing == True:
                valid = False
                break

            if not ((line[i] - line[i+1]) >= 1 and (line[i] - line[i+1]) <= 3):
                valid = False
                break

    return valid

for line in file.readlines():
    line = [int(num) for num in line.rstrip().split(" ")]
    

    for i in range(len(line)):
        if check_valid(line[:i] + line[i + 1:]):
            safe += 1
            break

print(safe)



    