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

print(sum([tiles[i] for i in tiles]))