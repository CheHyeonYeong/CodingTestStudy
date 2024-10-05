def solution(t, p):
    answer = 0
    for num in range(len(t)-len(p)+1):
        if (t[num:num+len(p)] <= p):
            answer += 1
    return answer