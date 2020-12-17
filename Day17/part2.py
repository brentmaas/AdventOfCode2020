import numpy as np

cubes = {}
inp = []
with open("Input.txt", "r") as f:
    l = f.readline().rstrip("\n")
    while l:
        inp.append([0] * 7 + [1 if c == "#" else 0 for c in l] + [0] * 7)
        l = f.readline().rstrip("\n")
cubes[0] = {0: np.array([[0] * len(inp[0])] * 7 + inp + [[0] * len(inp[0])] * 7, dtype=np.int32)}
for i in range(6):
    tmpcubes = {}
    for w in range(-i-1, i+2):
        tmpcubes[w] = {}
        for z in range(-i-1, i+2):
            tmpcubes[w][z] = np.copy(cubes[w][z]) if (w in cubes and z in cubes[w]) else np.zeros_like(cubes[0][0])
            n = np.zeros((tmpcubes[w][z].shape[0]-2, tmpcubes[w][z].shape[0]-2), dtype=np.int32)
            for dw in range(-1, 2):
                for dz in range(-1, 2):
                    if w + dw in cubes and z + dz in cubes[w+dw]:
                        n += cubes[w+dw][z+dz][:-2,:-2] + cubes[w+dw][z+dz][:-2,1:-1] + cubes[w+dw][z+dz][:-2,2:] + cubes[w+dw][z+dz][1:-1,:-2] + cubes[w+dw][z+dz][1:-1,2:] + cubes[w+dw][z+dz][2:,:-2] + cubes[w+dw][z+dz][2:,1:-1] + cubes[w+dw][z+dz][2:,2:]
                        if dz or dw:
                            n += cubes[w+dw][z+dz][1:-1,1:-1]
            tmpcubes[w][z][1:-1,1:-1][n == 3] = 1
            tmpcubes[w][z][1:-1,1:-1][np.logical_not(np.logical_or(n == 2, n == 3))] = 0
    for w in tmpcubes:
        if not w in cubes:
            cubes[w] = {}
        for z in tmpcubes[w]:
            cubes[w][z] = tmpcubes[w][z]
print(sum([sum([np.sum(cubes[w][z]) for z in cubes[w]]) for w in cubes]))