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

def subgame(deck1, deck2):
    states1 = []
    states2 = []
    while len(deck1) > 0 and len(deck2) > 0:
        if deck1 in states1 and deck2 in states2:
            return deck1, []
        states1.append(deck1.copy())
        states2.append(deck2.copy())
        a, b = deck1.pop(0), deck2.pop(0)
        if a <= len(deck1) and b <= len(deck2):
            subdeck1, subdeck2 = subgame(deck1[:a].copy(), deck2[:b].copy())
            if len(subdeck2) == 0:
                deck1 += [a, b]
            elif len(subdeck1) == 0:
                deck2 += [b, a]
        elif a > b:
            deck1 += [a, b]
        else:
            deck2 += [b, a]
    return deck1, deck2

decks[0], decks[1] = subgame(decks[0], decks[1])

if len(decks[0]) == 0:
    print(np.sum(np.linspace(len(decks[1]), 1, len(decks[1]), dtype=np.int32) * np.array(decks[1])))
else:
    print(np.sum(np.linspace(len(decks[0]), 1, len(decks[0]), dtype=np.int32) * np.array(decks[0])))