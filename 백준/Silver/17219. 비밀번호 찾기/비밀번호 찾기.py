import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dic = {}
for _ in range(n):
    a,b = input().split()
    dic[a] = b
out=[]
for _ in range(m):
    out.append(dic[input().strip()])
print(*out, sep='\n')