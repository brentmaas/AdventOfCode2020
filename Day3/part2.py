lines = []
with open("Input.txt", "r") as f:
    l = f.readline()
    while l:
        lines.append(l.strip("\n"))
        l = f.readline()

def trees(dx, dy):
    trees = 0
    x = 0
    w = len(lines[0])
    for y in range(0, len(lines), dy):
        trees += int(lines[y][x] == "#")
        x = (x + dx) % w
    return trees

print(trees(1, 1) * trees(3, 1) * trees(5, 1) * trees(7, 1) * trees(1, 2))