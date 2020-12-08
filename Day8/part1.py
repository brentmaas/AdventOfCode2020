lines = []
with open("Input.txt", "r") as f:
    l = f.readline()
    while l:
        lines.append(l.rstrip("\n"))
        l = f.readline()
ran = [False] * len(lines)
ip = 0
acc = 0
while True:
    if ran[ip]:
        break
    op, arg = lines[ip].split(" ")
    if op == "jmp":
        ip += int(arg) - 1
    elif op == "acc":
        acc += int(arg)
    ran[ip] = True
    ip += 1
print(acc)