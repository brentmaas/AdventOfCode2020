masks = [2 ** 36 - 1, 0]

def applymask(x):
    return (x & masks[0]) | masks[1]

def setmask(l):
    i = 1
    masks[0] = 2 ** 36 - 1
    masks[1] = 0
    for j in range(35, -1, -1):
        if l[j] == "1":
            masks[1] += i
        elif l[j] == "0":
            masks[0] -= i
        i = i << 1

mem = {}

with open("Input.txt", "r") as f:
    l = f.readline().rstrip("\n")
    while l:
        if l.startswith("mask = "):
            setmask(l[7:])
        else:
            address = int(l[4:].split("]")[0])
            mem[address] = applymask(int(l.split(" = ")[1]))
        l = f.readline().rstrip("\n")

print(sum([mem[i] for i in mem]))