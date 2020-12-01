import numpy as np

data = np.loadtxt("Input.txt", dtype=np.int32)
sums = data[:,np.newaxis] + data[np.newaxis,:]
for i in np.where(sums == 2020):
    if not i[0] == i[1]:
        print(data[i[0]] * data[i[1]])