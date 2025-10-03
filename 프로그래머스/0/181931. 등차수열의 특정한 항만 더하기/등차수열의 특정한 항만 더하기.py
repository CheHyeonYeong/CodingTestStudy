def solution(a, d, included):
    answer = 0
    for x,y in enumerate(included):
        print(x,y)
        if y == True:
            answer += a + x*d
    return answer