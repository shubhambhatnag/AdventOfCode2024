import heapq
import os


file = open("day1/input.txt","r")

heap1 = []
heap2 = []
for line in file.readlines():
    line = line.rstrip().split("   ")
    heapq.heappush(heap1,int(line[0]))
    heapq.heappush(heap2,int(line[1]))

total = 0

while heap1:
    total += abs(heapq.heappop(heap1)- heapq.heappop(heap2))


print(total)


    