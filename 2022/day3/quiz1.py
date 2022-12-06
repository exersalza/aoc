# find the same letter in each string

def get_prio(x: str):
    if x.islower():
        return ord(x) - ord('a') + 1
    return ord(x) - ord('A') + 27


ret = 0
tep = []
quiz2 = []

g = True

with open("input", 'r') as f:
    for i, line in enumerate(f):
        if i % 3 == 0:
            temp = []
            quiz2.append(temp)

        line.strip()
        first, sec = line[:len(line) // 2], line[len(line) // 2:]
        temp.append(line)

        for v in first:
            if v in sec:
                ret += get_prio(v)
                break


print(ret)

ret = 0
for a, b, c in quiz2:
    for i in a:
        if i in b and i in c:
            ret += get_prio(i)
            break


print(ret)
