import sys
input = sys.stdin.readline

M = int(input())
S = set()  # 🔥 여기 중요

for _ in range(M):
    T = input().strip()

    if T == "all":
        S = set(range(1, 21))

    elif T == "empty":
        S = set()

    else:
        a, b = T.split()
        b = int(b)

        if a == "add":
            S.add(b)

        elif a == "remove":
            S.discard(b)  # 안전

        elif a == "toggle":
            if b in S:
                S.discard(b)
            else:
                S.add(b)

        elif a == "check":
            print(1 if b in S else 0)