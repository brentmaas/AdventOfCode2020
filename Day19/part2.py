rules = {}
matches = 0

def check_old(text, rule, start=0):
    match = False
    i = []
    for r in rule:
        j = start
        m = True
        for c in r:
            if type(c) == int:
                m, k = check_old(text, rules[c], start=j)
                if len(k) > 1:
                    print("oef")
                j = min(k) if len(k) > 0 else len(text) + 1
            elif type(c) == str:
                m = text[j:j+len(c)] == c
                j += len(c)
            if not m:
                break
        if m:
            match = True
            i.append(j)
    return match, i

def check(text, rule, start=[0]):
    match = []
    i = []
    for j in range(len(start)):
        for r in rule:
            k = [start[j]]
            m = [True]
            for c in r:
                if type(c) == int:
                    m, k = check(text, rules[c], start=k)
                elif type(c) == str:
                    for l in range(len(k)):
                        m[l] = text[k[l]:k[l]+len(c)] == c
                        k[l] += len(c)
                for l in range(len(k)-1, -1, -1):
                    if not m[l]:
                        m.pop(l)
                        k.pop(l)
                if len(m) == 0:
                    break
            if len(m) > 0:
                match += m
                i += k
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
    rules[8] = [[42], [42, 8]]
    rules[11] = [[42, 31], [42, 11, 31]]
    l = f.readline().rstrip("\n")
    while l:
        test = check(l, rules[0])
        if True in test[0] and len(l) in test[1]:
            matches += 1
        l = f.readline().rstrip("\n")

print(matches)