import sys
from collections import deque

input = sys.stdin.readline
d = deque()
n = int(input())
out = []

for _ in range(n):
    command = input().split()

    if command[0] == "push_front":
        d.appendleft(command[1])
    elif command[0] == "push_back":
        d.append(command[1])
    elif command[0] == "pop_front":
        out.append(d.popleft() if d else "-1")
    elif command[0] == "pop_back":
        out.append(d.pop() if d else "-1")
    elif command[0] == "size":
        out.append(str(len(d)))
    elif command[0] == "empty":
        out.append("0" if d else "1")
    elif command[0] == "front":
        out.append(d[0] if d else "-1")
    elif command[0] == "back":
        out.append(d[-1] if d else "-1")

print("\n".join(out))
