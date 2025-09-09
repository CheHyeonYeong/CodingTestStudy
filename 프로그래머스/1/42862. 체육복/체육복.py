def solution(n, lost, reserve):
    
    lost_copy = [x for x in lost]
    
    for i in lost:
        if i in reserve:
            lost_copy.remove(i)
            reserve.remove(i)

    lost.sort()
    for s in lost:  
        if (s - 1) in reserve and s in lost_copy:
            lost_copy.remove(s)
            reserve.remove(s - 1)
        elif s + 1 in reserve and s in lost_copy:  
            lost_copy.remove(s)
            reserve.remove(s + 1)
            
    return n - len(lost_copy)
