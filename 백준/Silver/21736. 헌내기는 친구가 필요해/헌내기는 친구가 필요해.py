
import sys
from collections import deque
input = sys.stdin.readline

dx = [0,0,1,-1]
dy = [1,-1,0,0]

n,m = map(int, input().split()) # n = h = y, m = w = x
dq = deque()
people = []

count = 0
visited = [[False] * m for _ in range(n)]

for i in range(n):
    people.append(input().strip())

for i in range(n):
    for j in range(m):
        if people[i][j] == "I":
            dq.appendleft((i, j))
            visited[i][j] = True
            break
while dq:
    y,x = dq.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n and people[ny][nx] != "X" and not visited[ny][nx] :
            visited[ny][nx] = True
            if people[ny][nx] == "P":
                count += 1
            dq.append((ny, nx))
print(count if count > 0 else "TT")