lines = []
with open("Input.txt", "r") as f:
    l = f.readline()
    while l:
        lines.append(l.rstrip("\n"))
        l = f.readline()
done = False
i = 0
while not done:
    if lines[i].split(" ")[0] == "jmp":
        lines[i] = "nop " + lines[i].split(" ")[1]
    elif lines[i].split(" ")[0] == "nop":
        lines[i] = "jmp " + lines[i].split(" ")[1]
    else:
        i += 1
        continue
    ran = [False] * len(lines)
    ip = 0
    acc = 0
    while True:
        if ran[ip]:
            break
        op, arg = lines[ip].split(" ")
        ran[ip] = True
        if op == "jmp":
            ip += int(arg) - 1
        elif op == "acc":
            acc += int(arg)
        ip += 1
        if ip == len(lines):
            done = True
            break
    if lines[i].split(" ")[0] == "jmp":
        lines[i] = "nop " + lines[i].split(" ")[1]
    elif lines[i].split(" ")[0] == "nop":
        lines[i] = "jmp " + lines[i].split(" ")[1]
    i += 1
print(acc)