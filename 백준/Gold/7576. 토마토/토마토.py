
import sys
from collections import deque
input = sys.stdin.readline

w,h = map(int,input().strip().split())
tomatos = []
for _ in range(h):
    tomatos.append(list(map(int, input().strip().split())))
dq = deque([])
dx = [1,-1,0,0]
dy = [0,0,1,-1]

res = 0

for i in range(h):
    for j in range(w):
        if tomatos[i][j] == 1:
            dq.append([i,j])

def bfs():
    while dq:
        y,x = dq.popleft()
        for i in range(4):
            nx,ny = x+dx[i], y + dy[i]
            if 0 <= nx < w and 0 <= ny < h and tomatos[ny][nx] == 0:
                tomatos[ny][nx] = tomatos[y][x] + 1
                dq.append([ny,nx])

bfs()
for i in tomatos:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    res = max(res, max(i))
print(res-1)
