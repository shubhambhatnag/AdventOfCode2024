file = open("day4/input.txt","r")

word_search = []
for line in file.readlines():
    line = line.rstrip()
    word_search.append(list(line))


count = 0

for row in range(1,len(word_search) - 1):
    for col in range(1, len(word_search[0]) - 1):
        if word_search[row][col] == 'A':
            mas1 = word_search[row - 1][col - 1] + word_search[row + 1][col + 1]
            mas2 = word_search[row - 1][col + 1] + word_search[row + 1][col - 1]

            
            if sorted(mas1) == ['M','S'] and sorted(mas2) == ['M','S']:
                count += 1
            
            

print(count)
