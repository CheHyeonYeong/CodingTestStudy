
T = int(input())
for _ in range(T):
    n = int(input())
    dir1 = {}
    for _ in range(n):
        a,b = input().split()
        if b in dir1:
            dir1[b] +=1
        else:
            dir1[b] = 1

    result = 1
    for count in dir1.values():
        result *= (count + 1)

    print(result - 1)

