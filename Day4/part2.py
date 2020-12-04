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
        if 1920 <= int(pp["byr"]) <= 2002 and 2010 <= int(pp["iyr"]) <= 2020 and 2020 <= int(pp["eyr"]) <= 2030 and ((pp["hgt"].endswith("cm") and 150 <= int(pp["hgt"][:-2]) <= 193) or (pp["hgt"].endswith("in") and 59 <= int(pp["hgt"][:-2]) <= 76)) and pp["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"] and len(pp["pid"]) == 9 and pp["hcl"].startswith("#") and len(pp["hcl"]) == 7:
            v = True
            for c in pp["hcl"][1:]:
                if not c in "0123456789abcdef":
                    v = False
                    break
            for c in pp["pid"]:
                if not c in "0123456789":
                    v = False
                    break
            if v:
                valid += 1

print(valid)