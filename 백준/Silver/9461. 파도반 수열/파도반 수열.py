T = int(input())
for _ in range(T):
    n = int(input())
    p =[0] * max((n+1), 6)
    p[1] = 1
    p[2] = 1
    p[3] = 1
    p[4] = 2
    p[5] = 2

    for i in range(6, n + 1):
        p[i] = p[i-1] + p[i-5]
    print(p[n])