import sys

input = sys.stdin.readline

n, m = map(int, input().split())
numbers = list(map(int, input().split()))

prefix = [0] * (n + 1)
for i in range(1, n + 1):
    prefix[i] = prefix[i - 1] + numbers[i - 1]

out = []
for _ in range(m):
    a, b = map(int, input().split())
    out.append(prefix[b] - prefix[a-1])

sys.stdout.write("\n".join(map(str, out)))
