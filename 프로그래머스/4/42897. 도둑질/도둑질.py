def solution(money):
    n = len(money)
    
    if n == 1:
        return money[0]
    if n == 2:
        return max(money[0], money[1])
    if n == 3:
        return max(money)
    
    def rob(start, end):
        """
        start부터 end까지의 집을 대상으로 최대 금액 계산
        """
        prev2 = 0  # dp[i-2]
        prev1 = 0  # dp[i-1]
        
        for i in range(start, end):
            current = max(prev1, money[i] + prev2)
            prev2 = prev1
            prev1 = current
        
        return prev1
    
    # 경우 1: 첫 집 포함 (0 ~ n-2)
    case1 = rob(0, n - 1)
    
    # 경우 2: 첫 집 제외 (1 ~ n-1)
    case2 = rob(1, n)
    
    return max(case1, case2)
