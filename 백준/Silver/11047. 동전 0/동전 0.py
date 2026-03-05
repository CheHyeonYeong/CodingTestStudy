import sys
input = sys.stdin.readline

n, m = map(int, input().split())
coins = []
start = n
for i in range(n):
    coin = int(input())
    coins.append(coin)
    if coins[-1] > m:
        start = i
count = 0

for i in range(start-1, -1, -1):
    count += m//coins[i]
    m = m%coins[i]
print(count)