import numpy as np

seats = []
with open("Input.txt", "r") as f:
    l = f.readline()
    #Zeros padded around for easier neighbour calculation
    seats.append([0] * (len(l) + 1))
    while l:
        seats.append([0] + [(1 if c == "L" else 0) for c in l.rstrip("\n")] + [0])
        l = f.readline()
    seats.append([0] * len(seats[0]))
seats = np.array(seats, dtype=np.int32)

occ = np.zeros_like(seats)
while True:
    newocc = np.copy(occ)
    neighbours = occ[:-2,:-2] + occ[:-2,1:-1] + occ[:-2,2:] + occ[1:-1,:-2] + occ[1:-1,2:] + occ[2:,:-2] + occ[2:,1:-1] + occ[2:,2:]
    newocc[1:-1,1:-1][np.logical_and(seats[1:-1,1:-1] == 1, neighbours == 0)] = 1
    newocc[1:-1,1:-1][np.logical_and(occ[1:-1,1:-1] == 1, neighbours >= 4)] = 0
    
    if np.all(newocc == occ):
        break
    occ = newocc
print(np.sum(occ))