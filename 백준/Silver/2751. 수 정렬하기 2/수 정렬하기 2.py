import sys
input = sys.stdin.readline

n = int(input())
numbers = []
for _ in range(n):
    numbers.append(int(input().strip()))

numbers.sort()
print("\n".join(map(str,numbers)))