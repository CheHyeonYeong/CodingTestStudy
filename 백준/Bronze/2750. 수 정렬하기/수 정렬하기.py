
n = int(input())
answer = [0] * n
for i in range(n):
    answer[i] = int(input())
answer.sort()
for i in answer:
    print(i)