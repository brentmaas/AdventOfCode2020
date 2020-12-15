import numpy as np

nums = np.loadtxt("Input.txt", delimiter=",", dtype=np.int32)

occ = {}
last = nums[-1]
for i in range(len(nums)-1):
    occ[nums[i]] = i

for i in range(len(nums)-1, 2019):
    if last in occ:
        newlast = i - occ[last]
        occ[last] = i
        last = newlast
    else:
        occ[last] = i
        last = 0

print(last)