
import sys
from array import array

input = sys.stdin.buffer.readline
write = sys.stdout.write

n = int(input())
count = array('i',
              [0] * 10001)  # C 스타일 int 배열

for _ in range(n):
    count[int(input())] += 1

for i in range(1, 10001):
    c = count[i]
    if c:
        s = str(i) + '\n'
        while c > 10000:
            write(s * 10000)
            c -= 10000
        write(s * c)