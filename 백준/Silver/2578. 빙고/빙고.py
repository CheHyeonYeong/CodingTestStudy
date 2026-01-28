
bingo = []
order = []
for _ in range(5):
    bingo.append(list(map(int, input().split())))
for _ in range(5):
    order += list(map(int, input().split()))


pos = {}
for r in range(5):
    for c in range(5):
        pos[bingo[r][c]] = (r, c)

# 지워졌는지 체크하는 판
checked = [[False] * 5  for _ in range(5)]

def count_bingo():
    count = 0
    # 가로 5줄
    for r in range(5):
        if all(checked[r][c] for c in range(5)):
            count += 1

    # 세로 5줄
    for c in range(5):
        if all(checked[r][c] for r in range(5)):
            count += 1

    if all(checked[i][i] for i in range(5)):
        count += 1

    if all(checked[i][4-i] for i in range(5)):
        count += 1
    return count


for i, num in enumerate(order):
    r, c = pos[num]
    checked[r][c] = True
    if count_bingo() >= 3:
        print(i + 1)
        break     