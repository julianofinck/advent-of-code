"""
Ceres Search (for XMAS)
Ceres monitoring station
"""
# Read
numb_xmas = 0
with open("04/word_search.txt", "r") as f:
    matrix = [l.replace("\n", "") for l in f.readlines()]

# Part 1: find "XMAS" in every direction
# Horizontal
for line in matrix:
    numb_xmas += line.count("XMAS")
    numb_xmas += line.count("SAMX")

# Vertical
for m in [matrix, matrix[::-1]]:
    for j in range(len(m[0])):
        for i in range(0, len(m) - 3):
            word = ""
            for k in range(4):
                word += m[i + k][j]
            if word == "XMAS":
                numb_xmas += 1

# Diagonal
len_i = len(matrix) - 1
len_j = len(matrix[0]) - 1

for m in [matrix, [l[::-1] for l in matrix]]:
    i = len_i - 3
    j = 0
    upwards = True
    diagonals = list()
    while not (i == 0 and j == len_j - 2):
        diagonal = ""
        if i == 0 and j == 0:
            print(123)
        while not(i > len_i or j > len_j):
            diagonal += m[i][j]
            i += 1
            j += 1
        
        diagonals += [diagonal]

        # Set starting point
        if upwards:
            i = len_i - 3 - len(diagonals)
            j = 0
        else:
            i = 0
            j = len(diagonals) - len_i + 3

        # Change direction
        if i == 0 and j == 0:
            upwards = False

    for diagonal in diagonals:
        numb_xmas += diagonal.count("XMAS")
        numb_xmas += diagonal.count("SAMX")

print("Nº xmas:", numb_xmas)
    

# Part 2: find "MAS" crosses
numb_x_mas = 0
for i in range(1, len(matrix) - 1):
    for j in range(1, len(matrix) - 1):
        if matrix[i][j] == "A":
            tl_lr = matrix[i-1][j-1] + matrix[i+1][j+1]
            ll_tr = matrix[i+1][j-1] + matrix[i-1][j+1]
            if all([diag in ("SM", "MS") for diag in [tl_lr, ll_tr]]):
                numb_x_mas += 1

print("Nº cross mas:", numb_x_mas)
