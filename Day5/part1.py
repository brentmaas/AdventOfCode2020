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

highest = 0
with open("Input.txt", "r") as f:
    l = f.readline()
    while l:
        r, c = decode(l.strip("\n"))
        id = r * 8 + c
        if id > highest:
            highest = id
        l = f.readline()
print(highest)