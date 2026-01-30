def solution(money):
    n = len(money)
    
    if n == 1:
        return money[0]
    if n == 2:
        return max(money[0], money[1])
    if n == 3:
        return max(money)
    
    def rob(start, end):
        dp = [0] * (n+1)
        for i in range(start, end):
            dp[i] = max(dp[i-1], money[i] + dp[i-2])
        
        return dp[end-1]
    
    # 경우 1: 첫 집 포함 (0 ~ n-2)
    case1 = rob(0, n - 1)
    
    # 경우 2: 첫 집 제외 (1 ~ n-1)
    case2 = rob(1, n)
    
    return max(case1, case2)
