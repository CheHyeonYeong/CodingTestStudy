def DFS(k, cnt, dungeons, ch):
    global answer
    answer = max(answer, cnt)
    for i in range(len(dungeons)):
        if ch[i] == 0:
            if k >= dungeons[i][0]:
                ch[i] = 1
                DFS(k-dungeons[i][1], cnt + 1, dungeons, ch)
                ch[i] = 0
    
def solution(k, dungeons):
    global answer
    n = len(dungeons)
    ch = [0] * n
    answer = 0
    DFS(k, 0, dungeons, ch)
    return answer