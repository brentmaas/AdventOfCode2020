#dirs = ["E", "N", "W", "S"]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
x, y, dir = 0, 0, 0

with open("Input.txt", "r") as f:
    l = f.readline()
    while l:
        c, val = l[0], int(l.rstrip("\n")[1:])
        if c == "F":
            x += val * dx[dir]
            y += val * dy[dir]
        elif c == "L":
            dir = (dir + val // 90) % 4
        elif c == "R":
            dir = (dir - val // 90) % 4
        elif c == "E":
            x += val
        elif c == "N":
            y += val
        elif c == "W":
            x -= val
        elif c == "S":
            y -= val
        else:
            print(f"Unknown character: {c}")
        l = f.readline()
print(abs(x) + abs(y))