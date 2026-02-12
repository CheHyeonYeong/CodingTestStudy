n = int(input())

dots = []
for _ in range(n):
    dots.append(list(map(int, input().split())))

dots.sort()
for i in range(n):
    print(" ".join(map(str, dots[i])))