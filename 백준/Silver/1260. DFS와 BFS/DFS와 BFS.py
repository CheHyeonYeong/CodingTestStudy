
import sys
from collections import deque

n,m,v = map(int, sys.stdin.readline().split())

# 간선 만들기
graph = [[0] * (n+1) for _ in range(n+1)]
for i in range(m):
    x,y = map(int, sys.stdin.readline().split())
    graph[x][y] = graph[y][x] = 1

dfsVisited = [False] * (n+1)
bfsVisited = [False] * (n+1)

def dfs(v): #depth
    dfsVisited[v] = True
    print(v, end=' ')
    for i in range(1,n+1):
        if graph[v][i] == 1 and dfsVisited[i] == False:
            dfs(i)

def bfs(v): # breath
    queue = deque([v])
    bfsVisited[v] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in range(1,n+1):
            if graph[v][i] == 1 and bfsVisited[i] == False:
                queue.append(i)
                bfsVisited[i] = True

dfs(v)
print()
bfs(v)