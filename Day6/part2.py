group = {}
sum = 0
newgroup = True
with open("Input.txt", "r") as f:
    l = f.readline()
    while l:
        if l == "\n":
            sum += len(group)
            group = {}
            newgroup = True
        elif newgroup:
            for c in l.rstrip("\n"):
                group[c] = True
            newgroup = False
        else:
            remove = []
            for c in group:
                if not c in l:
                    remove.append(c)
            for c in remove:
                group.pop(c)
        l = f.readline()
sum += len(group)
print(sum)