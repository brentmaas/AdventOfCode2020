masks = [2 ** 35 - 1, 0]
flucs = []

def applymask(x):
    return (x & masks[0]) | masks[1]

def setmask(l):
    i = 1
    masks[0] = 2 ** 35 - 1
    masks[1] = 0
    flucs.clear()
    for j in range(35, -1, -1):
        if l[j] == "1":
            masks[1] += i
        elif l[j] == "X":
            masks[0] -= i
            flucs.append(i)
        i = i << 1

mem = {}

with open("Input.txt", "r") as f:
    l = f.readline().rstrip("\n")
    while l:
        if l.startswith("mask = "):
            setmask(l[7:])
        else:
            address = applymask(int(l[4:].split("]")[0]))
            val = int(l.split(" = ")[1])
            if len(flucs) > 0:
                for i in range(2 ** len(flucs)):
                    mem[address+sum([flucs[j] for j in range(len(flucs)) if (i & (2 ** j))])] = val
            else:
                mem[address] = val
        l = f.readline().rstrip("\n")

print(sum([mem[i] for i in mem]))