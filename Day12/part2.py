x, y = 0, 0
wx, wy = 10, 1

with open("Input.txt", "r") as f:
    l = f.readline()
    while l:
        c, val = l[0], int(l.rstrip("\n")[1:])
        if c == "F":
            x += val * wx
            y += val * wy
        elif c == "L":
            r = val // 90
            wx, wy = [1, 0, -1, 0][r] * wx + [0, -1, 0, 1][r] * wy, [0, 1, 0, -1][r] * wx + [1, 0, -1, 0][r] * wy
        elif c == "R":
            r = val // 90
            wx, wy = [1, 0, -1, 0][r] * wx + [0, 1, 0, -1][r] * wy, [0, -1, 0, 1][r] * wx + [1, 0, -1, 0][r] * wy
        elif c == "E":
            wx += val
        elif c == "N":
            wy += val
        elif c == "W":
            wx -= val
        elif c == "S":
            wy -= val
        else:
            print(f"Unknown character: {c}")
        l = f.readline()
print(abs(x) + abs(y))