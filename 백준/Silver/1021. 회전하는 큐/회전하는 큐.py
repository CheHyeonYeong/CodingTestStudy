import sys
from collections import deque

n,m = map(int, sys.stdin.readline().split())
d = deque([x for x in range(1,n+1)])
w = list(map(int, sys.stdin.readline().split()))

count = 0
for num in w:
    while True :
        if d[0] == num:
            d.popleft()
            break
        else:
            if d.index(num) <= len(d)//2:
                d.rotate(-1)
                count += 1
            else :
                d.rotate(1)
                count +=1
print(count)