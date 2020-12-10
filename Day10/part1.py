import numpy as np

data = np.sort(np.loadtxt("Input.txt", dtype=np.int32))
diffs = data[1:] - data[:-1]
diffs1 = np.sum(diffs == 1) + (data[0] == 1)
diffs3 = np.sum(diffs == 3) + (data[0] == 3) + 1
print(diffs1 * diffs3)