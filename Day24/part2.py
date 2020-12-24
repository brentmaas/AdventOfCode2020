tiles = {}
with open("Input.txt", "r") as f:
    l = f.readline().rstrip("\n")
    while l:
        i = 0
        x, y = 0, 0
        while i < len(l):
            if i < len(l) - 1:
                if l[i:i+2] == "sw":
                    y -= 1
                    i += 2
                    continue
                elif l[i:i+2] == "se":
                    y -= 1
                    x += 1
                    i += 2
                    continue
                elif l[i:i+2] == "nw":
                    y += 1
                    x -= 1
                    i += 2
                    continue
                elif l[i:i+2] == "ne":
                    y += 1
                    i += 2
                    continue
            if l[i] == "w":
                x -= 1
                i += 1
            elif l[i] == "e":
                x += 1
                i += 1
        if (x, y) in tiles:
            tiles[(x, y)] = False
        else:
            tiles[(x, y)] = True
        l = f.readline().rstrip("\n")

def tile(tiles, x, y):
    n = 0
    if (x-1,y) in tiles:
        n += tiles[(x-1,y)]
    if (x+1,y) in tiles:
        n += tiles[(x+1,y)]
    if (x-1,y+1) in tiles:
        n += tiles[(x-1,y+1)]
    if (x+1,y-1) in tiles:
        n += tiles[(x+1,y-1)]
    if (x,y-1) in tiles:
        n += tiles[(x,y-1)]
    if (x,y+1) in tiles:
        n += tiles[(x,y+1)]
    return ((x,y) in tiles and tiles[(x,y)] and (n == 1 or n == 2)) or ((not (x,y) in tiles or not tiles[(x,y)]) and n == 2)

for i in range(100):
    newtiles = {}
    for i in tiles:
        if tiles[i]:
            newtiles[(i[0],i[1])] = tile(tiles, i[0], i[1])
            newtiles[(i[0]-1,i[1])] = tile(tiles, i[0]-1, i[1])
            newtiles[(i[0]+1,i[1])] = tile(tiles, i[0]+1, i[1])
            newtiles[(i[0]-1,i[1]+1)] = tile(tiles, i[0]-1, i[1]+1)
            newtiles[(i[0]+1,i[1]-1)] = tile(tiles, i[0]+1, i[1]-1)
            newtiles[(i[0]-1,i[1])] = tile(tiles, i[0]-1, i[1])
            newtiles[(i[0],i[1]+1)] = tile(tiles, i[0], i[1]+1)
    tiles = newtiles

print(sum([tiles[i] for i in tiles]))