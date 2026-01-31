
import sys
from collections import deque
# 각 테스트 케이스에 대해 필요한 최소의 배추흰지렁이 마리 수를 출력한다.

import sys

T = int(sys.stdin.readline())
for _ in range(T):
    # 배추밭 가로, 세로, 배추 개수
    m,n,k = map(int, sys.stdin.readline().split())
    data = [[0] * m for _ in range(n)]

    dx= [1,-1,0,0]
    dy = [0,0,1,-1]

    for _ in range(k):
        a,b = map(int, input().split())
        data[b][a] = 1

    visited = [[False]*m for _ in range(n)]

    def bfs(x, y):
        q = deque()
        q.append((x, y))
        visited[y][x] = True

        while q:
            sx, sy = q.popleft()
            for i in range(4):
                nx = sx + dx[i]
                ny = sy + dy[i]

                if 0 <= nx < m and 0 <= ny < n:
                    if data[ny][nx] == 1 and not visited[ny][nx]:
                        visited[ny][nx] = True
                        q.append((nx, ny))


    count = 0
    for y in range(n):
        for x in range(m):
            if data[y][x] == 1 and not visited[y][x]:
                bfs(x, y)
                count += 1

    print(count)