from collections import defaultdict

file = open("day5/input.txt","r")

prereq = defaultdict(list)

total = 0

update_start = False
for line in file.readlines():
    line = line.rstrip()

    if line == "":
        update_start = True
        continue
    
    if not update_start:
        line = line.split("|")

        prereq[line[1]].append(line[0])

    else:
        
        valid = True

        found = set()

        
        line = line.split(",")
        
        total_set = set(line)
        
        
        for page in line:
            
            for pre_page in prereq[page]:
                
                if pre_page in total_set and pre_page not in found:
                    valid = False
                    break
            else:
                found.add(page)
        
        if valid:
            total += int(line[len(line)//2])


print(total)




