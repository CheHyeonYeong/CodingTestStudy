def DFS(L, visited, n, computers):
    visited[L] = 1
    for com in range(n):  
        if L != com and computers[L][com] == 1:
            if visited[com] == 0:  
                DFS(com, visited, n, computers)  
    
def solution(n, computers):
    visited = [0] * n
    answer = 0
    for i in range(n):
        if visited[i] == 0:
            DFS(i, visited, n, computers)
            answer += 1
    return answer