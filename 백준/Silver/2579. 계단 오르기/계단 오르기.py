
import sys
input = sys.stdin.readline

x = int(input())
stairs = []
for _ in range(x):
    stairs.append(int(input()))

dp = [0] * x
if x ==0:
    print(0)
elif x == 1:
    print(stairs[0])
elif x == 2:
    print(stairs[0] + stairs[1])
else:
    dp[0] = stairs[0]
    dp[1] = stairs[0] + stairs[1]
    dp[2] = max(stairs[2] + stairs[0], stairs[2] + stairs[1])

    for i in range(3, x):
        dp[i] = max(stairs[i] + dp[i-2], stairs[i] + stairs[i-1] + dp[i-3])
    print(dp[x-1])