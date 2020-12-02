valid = 0
with open("Input.txt", "r") as f:
    l = f.readline()
    while l:
        low = int(l.split("-")[0])
        high = int(l.split("-")[1].split(" ")[0])
        char = l.split(":")[0][-1]
        password = l.split(" ")[-1]
        if (password[low - 1] == char) ^ (high - 1 < len(password) and password[high - 1] == char):
            valid += 1
        l = f.readline()
print(valid)