import numpy as np

def check(num, nums):
    sums = nums[:,np.newaxis] + nums[np.newaxis,:]
    return num in sums

def find(num, nums):
    sums = np.cumsum(nums)
    for i in range(nums.shape[0]-1):
        if num in sums:
            return i, i + np.where(sums == num)[0][0]
        sums = sums[1:] - nums[i]

preamble_len = 25
allnums = np.zeros(0, dtype=np.int32)
nums = np.zeros(0, dtype=np.int32)
with open("Input.txt", "r") as f:
    for _ in range(preamble_len):
        i = int(f.readline().rstrip("\n"))
        nums = np.append(nums, i)
        allnums = np.append(allnums, i)
    l = f.readline()
    while l:
        i = int(l.rstrip("\n"))
        if not check(i, nums):
            left, right = find(i, allnums)
            print(np.amin(allnums[left:right+1]) + np.amax(allnums[left:right+1]))
            break
        nums = np.append(nums[1:], i)
        allnums = np.append(allnums, i)
        l = f.readline()