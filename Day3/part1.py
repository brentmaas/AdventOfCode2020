lines = []
with open("Input.txt", "r") as f:
    l = f.readline()
    while l:
        lines.append(l.strip("\n"))
        l = f.readline()

trees = 0
x = 0
w = len(lines[0])
for y in range(len(lines)):
    trees += int(lines[y][x] == "#")
    x = (x + 3) % w
print(trees)