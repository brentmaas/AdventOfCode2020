busses = []
with open("Input.txt", "r") as f:
    time = int(f.readline().rstrip("\n"))
    for i in f.readline().rstrip("\n").split(","):
        if i.isdigit():
            busses.append((int(i) - (time % int(i)), int(i)))
busses.sort()
print(busses[0][0] * busses[0][1])