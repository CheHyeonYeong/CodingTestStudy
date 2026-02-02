a= list(map(int,input().split()))

answer = 0
for i in range(5):
    answer += a[i] ** 2
answer = str(answer)
print(answer[-1])