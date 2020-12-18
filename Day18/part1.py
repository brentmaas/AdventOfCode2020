problems = []
with open("Input.txt", "r") as f:
    l = f.readline()
    while l:
        problems.append(l.rstrip("\n"))
        l = f.readline()

def eval_problem(problem):
    curr = problem
    while "(" in curr:
        i = curr.index("(")
        j = 1
        k = i + 1
        while j > 0:
            if curr[k] == "(":
                j += 1
            elif curr[k] == ")":
                j -= 1
            k += 1
        curr = curr[:i] + str(eval_problem(curr[i+1:k-1])) + curr[k:]
    parts = [int(c) if c.isdigit() else c for c in curr.split(" ")]
    while len(parts) > 1:
        if parts[1] == "+":
            out = parts[0] + parts[2]
        elif parts[1] == "*":
            out = parts[0] * parts[2]
        parts = [out] + parts[3:]
    return parts[0]

answers = [eval_problem(p) for p in problems]
print(sum(answers))