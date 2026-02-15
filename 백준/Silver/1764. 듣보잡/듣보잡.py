# ==================================
import sys
input = sys.stdin.readline

m, n = map(int, input().strip().split())
mset = set(input().strip() for _ in range(m))
nset = set(input().strip() for _ in range(n))

result = sorted(mset & nset)

print(len(result))
print('\n'.join(result))