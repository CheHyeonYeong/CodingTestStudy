
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().strip().split())
maper = []
for _ in range(n):
    maper.append(list(map(int, input().strip().split())))

dist = [[-1] * m for _ in range(
    n)]  # 거리 배열 (-1로 초기화)
dq = deque([])
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(n):
    for j in range(m):
        if maper[i][j] == 2:
            dist[i][
                j] = 0  # 목표지점 거리 0
            dq.append([i, j])
        elif maper[i][j] == 0:
            dist[i][
                j] = 0  # 벽은 0 출력


def bfs():
    while dq:
        y, x = dq.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and dist[ny][nx] == -1:
                dist[ny][nx] = dist[y][x] + 1
                dq.append([ny, nx])


bfs()
for row in dist:
    print(" ".join(map(str, row)))
