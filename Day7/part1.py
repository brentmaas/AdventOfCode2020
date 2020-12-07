rules = {}
with open("Input.txt", "r") as f:
    l = f.readline()
    while l:
        lhs = l.split(" bags contain ")[0]
        rhs = l.split(" bags contain ")[1].rstrip("\n").rstrip(".")
        if rhs == "no other bags":
            rules[lhs] = {}
        else:
            contains = {}
            for c in rhs.split(", "):
                q = int(c.split(" ")[0])
                b = c.lstrip(f"{q} ").rstrip("s").rstrip("g").rstrip("a").rstrip("b").rstrip(" ")
                contains[b] = q
            rules[lhs] = contains
        l = f.readline()
valid = []
tocheck = ["shiny gold"]
while len(tocheck) > 0:
    b = tocheck.pop()
    for r in rules:
        if b in rules[r] and not r in valid and not r in tocheck:
            tocheck.append(r)
            valid.append(r)
print(len(valid))