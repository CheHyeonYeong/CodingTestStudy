
from collections import deque

k = int(input())
for _ in range(k):
    n,m = map(int, input().split())
    lst = list(map(int, input().split()))
    q = deque((i,p) for i, p in enumerate(lst))
    count = 0

    while q:
        idx, p = q.popleft()

        # 1. 일단 내가 제일 크다고 가정해요
        is_max = True

        # 2. 큐에 남아있는 것들을 하나씩 꺼내서 나보다 큰 게 있는지 확인해요
        for _, other_p in q:
            if other_p > p:
                is_max = False # 나보다 큰 게 있네!
                break          # 더 볼 것도 없이 확인 중단

        # 3. 확인 결과에 따라 행동해요
        if not is_max:
            # 나보다 큰 게 있었으니까 다시 뒤로 가요
            q.append((idx, p))
        else:
            # 내가 제일 크니까 인쇄해요
            count += 1
            if idx == m:
                print(count)
                break