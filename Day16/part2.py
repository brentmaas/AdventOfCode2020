fields = {}
tickets = []
with open("Input.txt", "r") as f:
    l = f.readline().rstrip("\n")
    while l:
        name = l.split(":")[0]
        r1 = [int(i) for i in l.split(": ")[1].split(" or ")[0].split("-")]
        r2 = [int(i) for i in l.split(": ")[1].split(" or ")[1].split("-")]
        fields[name] = (r1, r2)
        l = f.readline().rstrip("\n")
    _ = f.readline()
    l = f.readline().rstrip("\n")
    your = [int(i) for i in l.split(",")]
    _ = f.readline()
    _ = f.readline()
    l = f.readline().rstrip("\n")
    while l:
        tickets.append([int(i) for i in l.split(",")])
        l = f.readline().rstrip("\n")

def valid(x):
    for i in fields:
        if fields[i][0][0] <= x <= fields[i][0][1] or fields[i][1][0] <= x <= fields[i][1][1]:
            return True
    return False

toremove = []
for t in range(len(tickets)):
    for f in tickets[t]:
        if not valid(f):
            toremove.append(t)
            break
for i in toremove[::-1]:
    tickets.pop(i)

valids = {}
for f in fields:
    valids[f] = []
    for i in range(len(your)):
        v = True
        for j in range(len(tickets)):
            if not (fields[f][0][0] <= tickets[j][i] <= fields[f][0][1] or fields[f][1][0] <= tickets[j][i] <= fields[f][1][1]):
                v = False
                break
        valids[f].append(v)

solutions = {}
solved = [False] * len(your)
cancon = True
while cancon:
    cancon = False
    for f in valids:
        if not f in solutions:
            vals = [valids[f][i] * (not solved[i]) for i in range(len(your))]
            if sum(vals) == 1:
                i = vals.index(1)
                solutions[f] = i
                solved[i] = True
                cancon = True

ans = 1
for f in solutions:
    if f.startswith("departure"):
        ans *= your[solutions[f]]
print(ans)