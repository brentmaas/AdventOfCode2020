import numpy as np

def decode(line):
    row = 0
    column = 0
    for i in range(7):
        if line[i] == "B":
            row += 2 ** (6 - i)
    for i in range(3):
        if line[7+i] == "R":
            column += 2 ** (2 - i)
    return row, column

seats = np.ones((128, 8), dtype=np.bool)
with open("Input.txt", "r") as f:
    l = f.readline()
    while l:
        r, c = decode(l.strip("\n"))
        seats[r,c] = False
        l = f.readline()

ids = np.where(seats)[0] * 8 + np.where(seats)[1]
for i in ids:
    if not i - 1 in ids and not i + 1 in ids and not i == 0 and not i == 127 * 8 + 7:
        print(i)