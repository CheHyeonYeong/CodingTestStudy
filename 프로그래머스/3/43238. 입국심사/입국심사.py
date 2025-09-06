def solution(n, times):
    answer = 0
    times.sort()
    minTime, maxTime = 1, n * times[-1]
    while minTime <= maxTime:
        mid = (minTime + maxTime) // 2
        count = 0
        for time in times:
            count += mid // time
        if count >= n : 
            maxTime = mid -1
        else : 
            minTime = mid + 1
        
        answer = minTime
    return answer