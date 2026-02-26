from collections import deque
def solution(numbers, target):
    answer = 0
    dq = deque([(0,0)])
    while dq: 
        csum,idx = dq.popleft()
        if idx == len(numbers):
            if csum == target:
                answer += 1
        else:
            dq.append([csum + numbers[idx] , idx+1])
            dq.append([csum - numbers[idx] , idx+1])
    return answer


