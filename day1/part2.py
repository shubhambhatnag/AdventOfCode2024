from collections import defaultdict

file = open("day1/input.txt","r")

first_lst = []
second_occur = defaultdict(int)

for line in file.readlines():
    line = line.rstrip().split("   ")
    first_lst.append(int(line[0]))
    second_occur[int(line[1])] += 1

score = 0

for num in first_lst:
    score += num * second_occur[num]


print(score)


    