
N = input()
m = max(1, int(N) - len(N) * 9)

for i in range(m, int(N) + 1):
    k = [int(j) for j in str(i)]
    if int(N) == i + sum(k):
        print(i)
        break
else: print(0)