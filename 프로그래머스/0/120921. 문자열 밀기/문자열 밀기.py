def solution(A, B):
    answer = 0
    if A==B:
        return 0
    #A에서 B가 되어야 함
    
    for i in range(len(A)):
        A=A[-1]+A[0:len(A)-1]
        answer+=1
        if A==B:
            return answer
        
    return -1