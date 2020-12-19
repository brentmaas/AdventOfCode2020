rules = {}
matches = 0

def check(text, rule, start=0):
    match = False
    i = len(text) + 1
    for r in rule:
        j = start
        m = True
        for c in r:
            if type(c) == int:
                m, j = check(text, rules[c], start=j)
            elif type(c) == str:
                m = text[j:j+len(c)] == c
                j += len(c)
            if not m:
                break
        if m:
            match = True
            i = min(i, j)
    return match, i

with open("Input.txt", "r") as f:
    l = f.readline().rstrip("\n")
    while l:
        spl = l.split(": ")
        id = int(spl[0])
        rule = []
        r = []
        for c in spl[1].split(" "):
            if c == "|":
                rule.append(r)
                r = []
            elif c.isdigit():
                r.append(int(c))
            else:
                r.append(c.replace("\"", ""))
        rule.append(r)
        rules[id] = rule
        l = f.readline().rstrip("\n")
    l = f.readline().rstrip("\n")
    while l:
        test = check(l, rules[0])
        if test[0] and test[1] == len(l):
            matches += 1
        l = f.readline().rstrip("\n")

print(matches)