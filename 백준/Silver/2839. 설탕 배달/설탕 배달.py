
n = int(input())

answer = -1
for i in range(n//5, -1, -1):
    k = n - (5 * i)
    if k % 3 == 0:
        answer = i + (k//3)
        break
print(answer)