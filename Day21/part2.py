foods = []
occ = {}

with open("Input.txt", "r") as f:
    l = f.readline()
    while l:
        spl = l.split(" (contains ")
        foods.append([spl[0].split(" "), spl[1].rstrip(")\n").split(", ")])
        for food in spl[0].split(" "):
            if not food in occ:
                occ[food] = 1
            else:
                occ[food] += 1
        l = f.readline()

allergens = {}
for f, a in foods:
    for b in a:
        if not b in allergens:
            allergens[b] = f
        else:
            allergens[b] = [i for i in f if i in allergens[b]]

solved = {}
while len(allergens) > 0:
    for a in allergens:
        if len(allergens[a]) == 1:
            solved[a] = allergens[a][0]
            for b in allergens:
                if solved[a] in allergens[b]:
                    allergens[b].remove(solved[a])
            allergens.pop(a)
            break

al = [a for a in solved]
al.sort()
print(",".join([solved[a] for a in al]))