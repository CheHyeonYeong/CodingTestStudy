
import sys
from collections import deque
input = sys.stdin.readline

computer = int(input())
line = int(input())
graph = [[] for i in range(computer + 1)]
visited = [False] * (computer+1)

for _ in range(line):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
visited[1] = True
dq = deque([1])

while dq:
    c = dq.popleft()
    for x in graph[c]:
        if visited[x] == False:
            dq.appendleft(x)
            visited[x] = True

print(sum(visited) - 1)    