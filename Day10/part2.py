import numpy as np

data = np.sort(np.loadtxt("Input.txt", dtype=np.int64))
data = np.append(0, np.append(data, data[-1] + 3))
ways = np.zeros_like(data)
ways[-1] = 1
for i in range(ways.shape[0]-2, -1, -1):
    ways[i] = ways[i+1]
    if i + 2 < ways.shape[0] and data[i+2] - data[i] <= 3:
        ways[i] += ways[i+2]
    if i + 3 < ways.shape[0] and data[i+3] - data[i] <= 3:
        ways[i] += ways[i+3]
print(ways[0])