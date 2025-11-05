from collections import deque

def solution(maps):
    answer = 0
    mx = len(maps)
    my = len(maps[0])
    dx=[-1, 0, 1, 0]
    dy=[0, 1, 0, -1]
    Q=deque()
    Q.append((0, 0))
    
    dis = [[0] * my for _ in range(mx)]
    dis[0][0] = 1
    maps[0][0] = 0
    
    while Q:
        x,y = Q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 범위 체크와 방문 체크
            if 0<= nx < mx and 0<= ny < my and maps[nx][ny]==1:
                maps[nx][ny]=0
                dis[nx][ny] = dis[x][y] + 1
                Q.append((nx, ny))
    if dis[mx-1][my-1] == 0:
        return -1
    else : 
        return dis[mx-1][my-1]
    

