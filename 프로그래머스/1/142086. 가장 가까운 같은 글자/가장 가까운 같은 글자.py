def solution(s):
    answer = [-1]
    for i in range(1,len(s)):
        if s[i] in s[:i]:
            cnt = 1
            while s[i-cnt] != s[i]:
                cnt+=1
            answer.append(cnt)
        else:
            answer.append(-1)
    return answer