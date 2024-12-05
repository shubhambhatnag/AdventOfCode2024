from collections import defaultdict

file = open("day5/input.txt","r")

prereq = defaultdict(list)

total = 0
updates = []
update_start = False


def is_valid(line):
    found = set()

        
    
    total_set = set(line)
    
    
    for page in line:
        
        for pre_page in prereq[page]:
            
            if pre_page in total_set and pre_page not in found:
                return False

        else:
            found.add(page)


    return True

for line in file.readlines():
    line = line.rstrip()

    if line == "":
        update_start = True
        continue
    
    if not update_start:
        line = line.split("|")

        prereq[line[1]].append(line[0])

    else:
        
        line = line.split(",")
        cnt = 0
        if (not is_valid(line)):
            
            while not is_valid(line):
             
                found = set()
                
                total_set = set(line)
                
                swap = False
                for page in range(len(line)):
                    if swap:
                        break
                    for pre_page in prereq[line[page]]:
                        
                        if pre_page in total_set and pre_page not in found:
                            line[line.index(pre_page)], line[page] = line[page], line[line.index(pre_page)]
                            swap = True
                            break
                    else:
                        found.add(line[page])


            total += int(line[len(line)//2])



        

        
        
        

print(total)




