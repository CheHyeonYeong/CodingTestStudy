from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):
    # 102×102 크기: 0~101 인덱스 사용 (경계 처리 포함)
    MAX_SIZE = 102
    visited = [[0] * MAX_SIZE for _ in range(MAX_SIZE)]
    graph = [[-1] * MAX_SIZE for _ in range(MAX_SIZE)]  # -1: 빈공간
    
    # 좌표 2배 확대하여 직사각형 그리기
    for rect in rectangle:
        x1, y1, x2, y2 = map(lambda x: x * 2, rect)
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                # 내부는 0으로 채움
                if x1 < i < x2 and y1 < j < y2:
                    graph[i][j] = 0
                # 테두리는 1로 표시 (단, 이미 내부(0)가 아닐 때만)
                elif graph[i][j] != 0:
                    graph[i][j] = 1
    
    # BFS 시작
    cx, cy = characterX * 2, characterY * 2
    ix, iy = itemX * 2, itemY * 2
    
    q = deque([(cx, cy)])
    visited[cx][cy] = 1
    
    while q:
        x, y = q.popleft()
        
        if x == ix and y == iy:
            # 2배 확대했으므로 다시 2로 나눔
            return visited[x][y] // 2
        
        for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
            nx, ny = x + dx, y + dy
            
            # 102×102 크기라 범위 체크 불필요!
            if graph[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))
    
    return -1  # 도달 불가능한 경우