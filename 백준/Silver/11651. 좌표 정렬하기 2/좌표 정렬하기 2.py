
n = int(input())

dots = []
for _ in range(n):
    dots.append(list(map(int, input().split())))

dots.sort(key = lambda x: (x[1], x[0]))
for i in range(n):
    print(" ".join(map(str, dots[i])))