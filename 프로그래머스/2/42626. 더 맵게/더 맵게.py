import heapq

def solution(scoville, K):
    
    heapq.heapify(scoville)  # 
    answer = 0
    
    while scoville[0] < K:
        
        if len(scoville) == 1 and scoville[0] < K:
            return -1
        
        first = heapq.heappop(scoville)   
        second = heapq.heappop(scoville)  
        
        new_value = first + (second * 2)
        heapq.heappush(scoville, new_value)  
        answer += 1

    return answer