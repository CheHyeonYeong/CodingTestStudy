def solution(distance, rocks, n):
    rocks.sort()
    answer = 0
    s, e = 1,distance
    rocks.append(distance)
    while  s <= e:
        mid = (s + e) // 2
        removeRock = 0  
        pre = 0  # 이전 rock 거리
        
        for rock in rocks:
            if rock - pre < mid:
                removeRock += 1
            else:
                pre = rock
                
        if removeRock <= n:
            answer = mid
            s = mid + 1
        else:
            e = mid -1
                
    return answer