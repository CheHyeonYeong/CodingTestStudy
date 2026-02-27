import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dic = {}
dic2 = {}
for i in range(1,n+1):
    a = input().strip()
    dic[a] = i
    dic2[str(i)] = a

out = []
for _ in range(m):
    a = input().strip()

    if not a.isdigit():
        out.append(str(dic[a]))
    else:
        out.append(dic2[a])

print("\n".join(out))