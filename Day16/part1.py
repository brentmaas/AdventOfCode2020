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

tser = 0
for t in tickets:
    for f in t:
        if not valid(f):
            tser += f
print(tser)