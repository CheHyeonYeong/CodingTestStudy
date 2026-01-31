import sys
from collections import deque
dx = [1,-1,0,0, 1,1,-1,-1]
dy = [0,0,1,-1, 1,-1,1,-1]

def bfs(sx, sy):
    q = deque()
    q.append((sx, sy))
    visited[sx][sy] = True
    while q:
        x, y = q.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h and 0 <= ny < w:
                if not visited[nx][ny] and land[nx][ny] == 1:
                    visited[nx][ny] = True
                    q.append((nx, ny))

while True:
    w,h = map(int, sys.stdin.readline().split())
    if w == 0 and h == 0:
        break
    land = [list(map(int, sys.stdin.readline().split())) for i in range(h)]
    visited = [[False]* w for _ in range(h)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if land[i][j] == 1 and not visited[i][j]:
                bfs(i,j)
                cnt+=1
    print(cnt)
