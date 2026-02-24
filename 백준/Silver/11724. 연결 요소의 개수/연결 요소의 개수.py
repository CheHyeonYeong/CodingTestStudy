
import sys
from collections import deque
input = sys.stdin.readline

# 방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.

# 정점의 개수 n, 간선의 개수 m
n,m = map(int, input().split())
# 그래프부터 만들기
graph = [[] for _ in range(n+1)]

# bfs
def bfs(v):
    dp = deque([v])
    visited[v] = True
    while dp:
        node = dp.popleft()
        for next in graph[node]:
            if not visited[next]:
                visited[next] = True
                dp.append(next)

for _ in range(m): # 무방향이므로 간선의 양 끝점 u,v를 받아서 graph에 추가한다
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 방문여부 파악을 위한 리스트
visited = [False] * (n+1)

# 연결요소 개수 세기
count = 0

for i in range(1, n+1):
    if not visited[i]:
        bfs(i)
        count += 1
# 연결 요소의 개수 출력
print(count)