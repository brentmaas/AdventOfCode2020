passports = []
p = {}
with open("Input.txt", "r") as f:
    l = f.readline()
    while l:
        if l == "\n":
            passports.append(p)
            p = {}
        else:
            for i in l.strip("\n").split(" "):
                field, data = i.split(":")
                p[field] = data
        l = f.readline()
passports.append(p)

valid = 0
for pp in passports:
    if "byr" in pp and "iyr" in pp and "eyr" in pp and "hgt" in pp and "hcl" in pp and "ecl" in pp and "pid" in pp:
        valid += 1

print(valid)