valid = 0
with open("Input.txt", "r") as f:
    l = f.readline()
    while l:
        low = int(l.split("-")[0])
        high = int(l.split("-")[1].split(" ")[0])
        char = l.split(":")[0][-1]
        password = l.split(" ")[-1]
        occ = 0
        for c in password:
            if c == char:
                occ += 1
        if low <= occ <= high:
            valid += 1
        l = f.readline()
print(valid)