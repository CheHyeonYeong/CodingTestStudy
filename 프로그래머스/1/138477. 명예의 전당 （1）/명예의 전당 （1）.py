def solution(k, score):
    stack = []
    answer = []
    for i in range(len(score)):
        
        stack.append(score[i])    
        stack.sort(reverse = True)
        if (i>=k):
            stack.pop()
            
        answer.append(min(stack))
    return answer