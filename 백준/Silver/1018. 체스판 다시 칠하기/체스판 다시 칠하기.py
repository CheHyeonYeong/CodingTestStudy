
n,m = map(int, input().strip().split())
board = []
for _ in range(n):
    board.append(input().strip())

ans = 64
for w in range(n-7):
    for h in range(m-7):
        cnt = 0  # 패턴1과 다른 칸 수
        for i in range(8):
            for j in range(8):
                expected = 'W' if (i + j) % 2 == 0 else 'B'
                if board[w + i][h + j] != expected:
                    cnt += 1
        ans = min(ans, cnt, 64 - cnt)

print(ans)