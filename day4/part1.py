file = open("day4/input.txt","r")

word_search = []
for line in file.readlines():
    line = line.rstrip()
    word_search.append(list(line))


count = 0

for row in range(len(word_search)):
    for col in range(len(word_search[0])):
        if word_search[row][col] == 'X':
            if col + 3 < len(word_search[0]):
                word = word_search[row][col] + word_search[row][col+1] + word_search[row][col+2] + word_search[row][col+3]
                if word == "XMAS":
                    count += 1

            if row + 3 < len(word_search):
                word = word_search[row][col] + word_search[row+1][col] + word_search[row+2][col] + word_search[row+3][col]
                if word == "XMAS":
                    count += 1

            if col - 3 >= 0:
                word = word_search[row][col] + word_search[row][col-1] + word_search[row][col-2] + word_search[row][col-3]
                if word == "XMAS":
                    count += 1

            if row - 3 >= 0:
                word = word_search[row][col] + word_search[row-1][col] + word_search[row-2][col] + word_search[row-3][col]
                if word == "XMAS":
                    count += 1

            if row + 3 < len(word_search) and col + 3 < len(word_search[0]):
                word = word_search[row][col] + word_search[row+1][col+1] + word_search[row+2][col+2] + word_search[row+3][col+3]
                if word == "XMAS":
                    count += 1
                    
            if row + 3 < len(word_search) and col - 3 >= 0:
                word = word_search[row][col] + word_search[row+1][col-1] + word_search[row+2][col-2] + word_search[row+3][col-3]
                if word == "XMAS":
                    count += 1

            if row - 3 >= 0 and col + 3 < len(word_search[0]):
                word = word_search[row][col] + word_search[row-1][col+1] + word_search[row-2][col+2] + word_search[row-3][col+3]
                if word == "XMAS":
                    count += 1

            if row - 3 >= 0 and col - 3 >= 0:
                word = word_search[row][col] + word_search[row-1][col-1] + word_search[row-2][col-2] + word_search[row-3][col-3]
                if word == "XMAS":
                    count += 1

print(count)
