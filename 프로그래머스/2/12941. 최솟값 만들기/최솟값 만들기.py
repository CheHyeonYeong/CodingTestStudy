def solution(A,B):
    answer = 0
    A.sort()
    B.sort(reverse=True)
    for i in range(len(A)):
        print(A[i], B[i])
        answer += A[i]*B[i]
    return answer