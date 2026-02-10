
T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())
    dp = [[x for x in range(1,n+1)] for x in range(k+1)]
    for i in range(1,k+1):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    print(dp[k][n-1])

