inp = "523764819"

cups = [int(i) for i in inp]

i = 0
for _ in range(100):
    pickup = []
    for j in range(3):
        if i + 1 < len(cups):
            pickup.append(cups.pop(i+1))
        else:
            pickup.append(cups.pop(0))
            i -= 1
    mn, mx = min(cups), max(cups)
    k, l = None, cups[i] - 1
    while k is None:
        if l in cups:
            k = cups.index(l)
        else:
            l -= 1
            if l < mn:
                l = mx
    cups = cups[:k+1] + pickup + cups[k+1:]
    if k < i:
        i += 3
    i = (i + 1) % len(cups)
i = cups.index(1)
print("".join([str(cups[i+1+j-len(cups)]) for j in range(len(cups) - 1)]))