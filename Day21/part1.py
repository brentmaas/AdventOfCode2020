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

n = 0
for f in occ:
    isallergen = False
    for a in allergens:
        if f in allergens[a]:
            isallergen = True
            break
    if not isallergen:
        n += occ[f]

print(n)