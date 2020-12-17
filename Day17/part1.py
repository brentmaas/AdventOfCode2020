import numpy as np

cube = {}
inp = []
with open("Input.txt", "r") as f:
    l = f.readline().rstrip("\n")
    while l:
        inp.append([0] * 7 + [1 if c == "#" else 0 for c in l] + [0] * 7)
        l = f.readline().rstrip("\n")
cube[0] = np.array([[0] * len(inp[0])] * 7 + inp + [[0] * len(inp[0])] * 7, dtype=np.int32)
for i in range(6):
    tmpcube = {}
    for z in range(-i-1, i+2):
        tmpcube[z] = np.copy(cube[z]) if z in cube else np.zeros_like(cube[0])
        n = np.zeros((tmpcube[z].shape[0]-2, tmpcube[z].shape[0]-2), dtype=np.int32)
        for dz in range(-1, 2):
            if z + dz in cube:
                n += cube[z+dz][:-2,:-2] + cube[z+dz][:-2,1:-1] + cube[z+dz][:-2,2:] + cube[z+dz][1:-1,:-2] + cube[z+dz][1:-1,2:] + cube[z+dz][2:,:-2] + cube[z+dz][2:,1:-1] + cube[z+dz][2:,2:]
                if dz:
                    n += cube[z+dz][1:-1,1:-1]
        tmpcube[z][1:-1,1:-1][n == 3] = 1
        tmpcube[z][1:-1,1:-1][np.logical_not(np.logical_or(n == 2, n == 3))] = 0
    for z in tmpcube:
        cube[z] = tmpcube[z]
print(sum([np.sum(cube[z]) for z in cube]))