
import sys
n = int(sys.stdin.readline())
students = [0]*n
for i in range(n):
    students[i] = sys.stdin.readline().strip()
k = 1
while True:
    answer = set()
    for name in students:
        answer.add(name[-k:])
    if len(answer) == n:
        print(k)
        break
    k += 1