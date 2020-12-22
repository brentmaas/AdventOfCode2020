import numpy as np

decks = []
with open("Input.txt", "r") as f:
    l = f.readline()
    deck = []
    while l:
        if l.rstrip("\n").isdigit():
            deck.append(int(l.rstrip("\n")))
        elif l == "\n":
            decks.append(deck)
            deck = []
        l = f.readline()
    decks.append(deck)

while len(decks[0]) > 0 and len(decks[1]) > 0:
    a, b = decks[0].pop(0), decks[1].pop(0)
    if a > b:
        decks[0] += [a, b]
    else:
        decks[1] += [b, a]

if len(decks[0]) == 0:
    print(np.sum(np.linspace(len(decks[1]), 1, len(decks[1]), dtype=np.int32) * np.array(decks[1])))
else:
    print(np.sum(np.linspace(len(decks[0]), 1, len(decks[0]), dtype=np.int32) * np.array(decks[0])))