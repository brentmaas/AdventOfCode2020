import numpy as np

monsterlines = ["                  # ", "#    ##    ##    ###", " #  #  #  #  #  #   "]
monster = np.array([[c == " " for c in l] for l in monsterlines], dtype=np.int32)

tiles = {}
edges = {} #WSEN
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
corner0 = None
for i in corners:
    if edges[i][0] is None and edges[i][3] is None:
        corner0 = i
        break

for i in tiles:
    tiles[i] = tiles[i][1:-1,1:-1]

image = np.zeros((tiles[i].shape[0] * int(np.sqrt(len(tiles))), tiles[i].shape[1] * int(np.sqrt(len(tiles)))), dtype=np.int32)
for i in range(int(np.sqrt(len(tiles)))):
    for j in range(int(np.sqrt(len(tiles)))):
        k = corner0
        for _ in range(i):
            k = edges[k][1]
        for _ in range(j):
            k = edges[k][2]
        image[i*tiles[corner0].shape[0]:(i+1)*tiles[corner0].shape[0],j*tiles[corner0].shape[1]:(j+1)*tiles[corner0].shape[1]] = tiles[k]

imagenomonster = np.copy(image)
n = 0
for f in [0, 1, 2]:
    for r in [0, 1, 2, 3]:
        if f == 0:
            image_i = np.rot90(image, r)
        elif f == 1:
            image_i = np.rot90(np.fliplr(image), r)
        elif f == 2:
            image_i = np.rot90(np.flipud(image), r)
        n_i = 0
        for i in range(image.shape[0] - monster.shape[0]):
            for j in range(image.shape[1] - monster.shape[1]):
                if np.all(image_i[i:i+monster.shape[0],j:j+monster.shape[1]] + monster > 0):
                    image_i[i:i+monster.shape[0],j:j+monster.shape[1]][np.logical_not(monster)] = 2
                    n_i += 1
        if n_i > n:
            image_i[image_i == 2] = 0
            imagenomonster = image_i
            n = n_i
print(np.sum(imagenomonster))