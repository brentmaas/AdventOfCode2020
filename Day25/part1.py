with open("Input.txt", "r") as f:
    pkeycard = int(f.readline().rstrip("\n"))
    pkeydoor = int(f.readline().rstrip("\n"))

def getloopsize(pkey):
    i = 1
    j = 1
    while True:
        j *= 7
        j = j - int(j / 20201227) * 20201227
        if j == pkey:
            return i
        i += 1

def transform(snum, loopsize):
    j = 1
    for _ in range(loopsize):
        j *= snum
        j = j - int(j / 20201227) * 20201227
    return j

print(transform(pkeycard, getloopsize(pkeydoor)))