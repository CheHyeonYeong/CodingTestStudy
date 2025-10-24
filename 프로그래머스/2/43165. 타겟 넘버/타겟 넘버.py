answer = 0

def isTarget(numbers, ch):
    v_target = 0
    for i in range(len(numbers)):
        if ch[i] == 0:
            v_target += numbers[i]
        else:
            v_target -= numbers[i]
    return v_target

def DFS(L, numbers, ch, target):
    global answer
    
    # 종료 조건: 모든 숫자를 다 봤을 때
    if L == len(numbers):
        if isTarget(numbers, ch) == target:
            answer += 1
        return
    
    # 현재 숫자를 더하는 경우 (ch[L] = 0)
    ch[L] = 0
    DFS(L+1, numbers, ch, target)
    
    # 현재 숫자를 빼는 경우 (ch[L] = 1)
    ch[L] = 1
    DFS(L+1, numbers, ch, target)

def solution(numbers, target):
    global answer
    answer = 0
    ch = [0] * len(numbers)
    DFS(0, numbers, ch, target)
    return answer