group = {}
sum = 0
with open("Input.txt", "r") as f:
    l = f.readline()
    while l:
        if l == "\n":
            sum += len(group)
            group = {}
        else:
            for c in l[:-1]:
                group[c] = True
        l = f.readline()
sum += len(group)
print(sum)