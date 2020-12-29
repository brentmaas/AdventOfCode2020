inp = "523764819"
#inp = "389125467"

cups = [int(i) for i in inp] + [i for i in range(len(inp) + 1, 1000001)]

i = 0
for a in range(10000000):
    if not a % 1000:
        print(a)
    pickup = []
    for j in range(3):
        if i + 1 < len(cups):
            pickup.append(cups.pop(i+1))
        else:
            pickup.append(cups.pop(0))
            i -= 1
    mn = 1 if not 1 in pickup else 2 if not 2 in pickup else 3 if not 3 in pickup else 4
    mx = 1000000 if not 1000000 in pickup else 999999 if not 999999 in pickup else 999998 if not 999998 in pickup else 999997
    k, l = None, cups[i] - 1
    if l < mn:
        l = mx
    while k is None:
        if not l in pickup:
            k = cups.index(l)
        else:
            l -= 1
            if l < mn:
                l = mx
    cups[k+1:k+1] = pickup
    if k < i:
        i += 3
    i = (i + 1) % len(cups)
i = cups.index(1)
print(cups[(i+1)%len(cups)], cups[(i+2)%len(cups)])