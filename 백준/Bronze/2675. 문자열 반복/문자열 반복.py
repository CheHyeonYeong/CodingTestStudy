n = int(input())
for _ in range(n):
    T,s = input().split()
    T = int(T)
    s = list(s)
    print(''.join(x*T for x in s))
