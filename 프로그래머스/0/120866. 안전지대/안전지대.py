def solution(board):
    answer = 0
    dirs = [[-1,-1],[-1,0],[-1,1]
            ,[0,-1],[0,0],[0,1]
            ,[1,-1],[1,0],[1,1]]
    n, m = len(board), len(board[0])
    sdir = set()

    for i in range(n):
        for j in range(m):
            if board[i][j] != 1:
                continue
            for dx, dy in dirs:
                x = i + dx
                y = j + dy
                if x < 0 or x >= n or y < 0 or y >= m:
                    continue
                sdir.add((x, y))

    return n * m - len(sdir)
