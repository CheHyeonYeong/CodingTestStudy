import sys
input = sys.stdin.readline

n = int(input())

if n == 0:
    print(0)
    exit()

k = [0] * 31
for _ in range(n):
    k[int(input())] += 1

a = int(n * 0.15 + 0.5)

total = 0
for i in range(31):
    total += i * k[i]

# 작은 값 제거
remain = a
for i in range(31):
    if remain == 0:
        break
    remove = min(k[i], remain)
    total -= i * remove
    k[i] -= remove
    remain -= remove

# 큰 값 제거
remain = a
for i in range(30, -1, -1):
    if remain == 0:
        break
    remove = min(k[i], remain)
    total -= i * remove
    k[i] -= remove
    remain -= remove

remain_n = n - 2 * a
print(int(total / remain_n + 0.5))
