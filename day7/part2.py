file = open("day7/input.txt","r")



def apply(lst,target):
    if len(lst) == 1:
        return target == lst[0]
    return apply([lst[0] + lst[1]]+lst[2:], target) or apply([lst[0] * lst[1]]+lst[2:], target) or apply([int(str(lst[0]) + str(lst[1]))]+lst[2:], target) 
    
total = 0
for line in file.readlines():
    line = line.rstrip()
    line = line.split(": ")
    target = int(line[0])
    nums = [int(i) for i in line[1].split(" ")]

    if apply(nums,target):
        total += target


print(total)






