import numpy as np

tiles = {}
edges = {} #WNES
solved = {}

with open("Input.txt", "r") as f:
    l = f.readline()
    tile = []
    id = None
    while l:
        if l.startswith("Tile"):
            id = int(l[5:-2])
        elif l == "\n":
            tiles[id] = np.array(tile, dtype=np.int32)
            edges[id] = [None, None, None, None]
            solved[id] = False
            tile = []
            id = None
        else:
            tile.append([1 if c == "#" else 0 for c in l[:-1]])
        l = f.readline()

solved[[i for i in tiles.keys()][0]] = True

def check(i, j, r, f, e):
    if f == 0:
        a_i = np.rot90(tiles[i], r-e)[:,-1]
    if f == 1:
        a_i = np.rot90(np.fliplr(tiles[i]), r-e)[:,-1]
    elif f == 2:
        a_i = np.rot90(np.flipud(tiles[i]), r-e)[:,-1]
    b_i = np.rot90(tiles[j], -e)[:,0]
    return np.all(a_i == b_i)

while False in [solved[i] for i in solved]:
    for i in [a for a in solved if not solved[a]]:
        for j in [b for b in solved if solved[b] and sum([not c is None for c in edges[b]]) < 4]:
            for f in [0, 1, 2]:
                for r in [0, 1, 2, 3]:
                    for e in [0, 1, 2, 3]:
                        if check(i, j, r, f, e):
                            solved[i] = True
                            if f == 1:
                                tiles[i] = np.fliplr(tiles[i])
                            elif f == 2:
                                tiles[i] = np.flipud(tiles[i])
                            tiles[i] = np.rot90(tiles[i], r)
                            edges[i][(e + 2) % 4] = j
                            edges[j][e] = i
                            break
                    if solved[i]:
                        break
                if solved[i]:
                    break
            if solved[i]:
                break

while 1 in [sum([not j is None for j in edges[i]]) for i in solved]:
    for i in tiles:
        for j in [k for k in tiles if k in edges[i]]:
            e = edges[i].index(j)
            if edges[i][(e-1)%4] is None and not edges[j][(e-1)%4] is None and not edges[edges[j][(e-1)%4]][(e+2)%4] is None:
                edges[i][(e-1)%4] = edges[edges[j][(e-1)%4]][(e+2)%4]
                edges[edges[edges[j][(e-1)%4]][(e+2)%4]][(e+1)%4] = i
            if edges[i][(e+1)%4] is None and not edges[j][(e+1)%4] is None and not edges[edges[j][(e+1)%4]][(e+2)%4] is None:
                edges[i][(e+1)%4] = edges[edges[j][(e+1)%4]][(e+2)%4]
                edges[edges[edges[j][(e+1)%4]][(e+2)%4]][(e-1)%4] = i

corners = [i for i in tiles if sum([not j is None for j in edges[i]]) == 2]
print(corners[0] * corners[1] * corners[2] * corners[3])