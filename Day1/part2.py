import numpy as np

data = np.loadtxt("Input.txt", dtype=np.int32)
sums = data[:,np.newaxis,np.newaxis] + data[np.newaxis,:,np.newaxis] + data[np.newaxis,np.newaxis,:]
for i in np.where(sums == 2020):
    if not i[0] == i[1] and not i[0] == i[2] and not i[1] == i[2]:
        print(data[i[0]] * data[i[1]] * data[i[2]], data[i[0]], data[i[1]], data[i[2]])