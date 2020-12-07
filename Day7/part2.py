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
n = 0
bags = {"shiny gold": 1}
while len(bags) > 0:
    newbags = {}
    for b in bags:
        for c in rules[b]:
            if c in newbags:
                newbags[c] += bags[b] * rules[b][c]
            else:
                newbags[c] = bags[b] * rules[b][c]
            n += bags[b] * rules[b][c]
    bags = newbags
print(n)