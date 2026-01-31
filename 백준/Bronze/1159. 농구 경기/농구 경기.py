import sys
n = int(sys.stdin.readline())
people = []
for _ in range(n):
    people.append(sys.stdin.readline().strip())
dic = {}
for person in people:
    p = person[0]
    if p not in dic:
        dic[p] = 1
    else:
        dic[p] += 1
result = []
for k in sorted(dic):
    if dic[k] >= 5:
        result.append(k)

print("".join(map(str, result)) if result else "PREDAJA")