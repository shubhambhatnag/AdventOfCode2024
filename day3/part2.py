import re
file = open("day3/input.txt","r")

total = 0
for line in file.readlines():
    line = line.rstrip()
    curr = 0

    mul_pattern = r"mul\((\d{1,}),(\d{1,})\)"

    matches = re.finditer(mul_pattern, line)

    matches_with_start = [(match,match.start()) for match in matches]


    do_pattern = r"do\(\)"

    matches = re.finditer(do_pattern, line)

    do_set = set()

    for do in matches:
        do_set.add(do.start())


    dont_pattern = r"don\'t\(\)"

    matches = re.finditer(dont_pattern, line)

    dont_set = set()

    for dont in matches:
        dont_set.add(dont.start())


    for match, start in matches_with_start:
        e1, e2 = int(match.group(1)), int(match.group(2))
        
        do = True

        while start >= 0:
            if start in do_set:
                break
            if start in dont_set:
                do = False
                break

            start -= 1
        if do:
            total += e1 * e2



    

print(total)



        





    