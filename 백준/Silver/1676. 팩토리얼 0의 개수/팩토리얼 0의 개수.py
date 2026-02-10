
n = int(input())
answer = 0
m = 5
while True:
    if n // m == 0:
        break
    answer += n//m
    m *= 5
print(answer)
