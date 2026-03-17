T = int(input())
P = list(map(int, input().split()))

P.sort()
result = 0
for i in range(1,T+1):
    result += sum(P[:i])
print(result)