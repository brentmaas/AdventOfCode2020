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

def v(x, y, dx, dy):
    nx = x + dx
    ny = y + dy
    while not (seats[nx,ny] == 1 or nx == 0 or ny == 0 or nx == seats.shape[0] - 1 or ny == seats.shape[1] - 1):
        nx += dx
        ny += dy
    return nx, ny

#bl, b, br, r, tr, t, tl, l
dxs = [1, 1, 1, 0, -1, -1, -1, 0]
dys = [-1, 0, 1, 1, 1, 0, -1, -1]
visx = np.zeros((seats.shape[0], seats.shape[1], 8), dtype=np.int32)
visy = np.zeros((seats.shape[0], seats.shape[1], 8), dtype=np.int32)
for x in range(1, seats.shape[0]-1):
    for y in range(1, seats.shape[1]-1):
        for z in range(8):
            visx[x,y,z], visy[x,y,z] = v(x, y, dxs[z], dys[z])

occ = np.zeros_like(seats)
while True:
    newocc = np.copy(occ)
    #neighbours = occ[:-2,:-2] + occ[:-2,1:-1] + occ[:-2,2:] + occ[1:-1,:-2] + occ[1:-1,2:] + occ[2:,:-2] + occ[2:,1:-1] + occ[2:,2:]
    neighbours = np.sum(np.array([occ[visx[:,:,z],visy[:,:,z]] for z in range(8)]), axis=0)
    newocc[np.logical_and(seats == 1, neighbours == 0)] = 1
    newocc[np.logical_and(occ == 1, neighbours >= 5)] = 0
    
    if np.all(newocc == occ):
        break
    occ = newocc
print(np.sum(occ))