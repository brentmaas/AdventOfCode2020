import numpy as np

def check(num, nums):
    sums = nums[:,np.newaxis] + nums[np.newaxis,:]
    return num in sums

preamble_len = 25
nums = np.zeros(0, dtype=np.int32)
with open("Input.txt", "r") as f:
    for _ in range(preamble_len):
        nums = np.append(nums, int(f.readline().rstrip("\n")))
    l = f.readline()
    while l:
        if not check(int(l.rstrip("\n")), nums):
            print(int(l.rstrip("\n")))
            break
        nums = np.append(nums[1:], int(l.rstrip("\n")))
        l = f.readline()