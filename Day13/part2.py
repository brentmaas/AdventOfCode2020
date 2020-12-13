busses = []
with open("Input.txt", "r") as f:
    f.readline().rstrip("\n")
    spl = f.readline().rstrip("\n").split(",")
    for i in range(len(spl)):
        if spl[i].isdigit():
            busses.append((i, int(spl[i])))
t = busses[0][1]
dt = busses[0][1]
for i in range(1, len(busses)):
    while (t + busses[i][0]) % busses[i][1] != 0:
        t += dt
    dt *= busses[i][1]
print(t)