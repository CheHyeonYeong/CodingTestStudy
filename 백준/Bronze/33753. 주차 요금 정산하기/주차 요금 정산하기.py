import sys
a,b,c = map(int, sys.stdin.readline().split())
T = int(sys.stdin.readline())
answer = a
n = T-30
if n > 0:
    answer += n//b * c
    if n % b > 0 :
        answer += c
print(answer)