import sys
input = sys.stdin.readline

n = int(input())
target = [int(input()) for _ in range(n)]

stack = []
result = []
current = 1

for num in target:
    #num을 pop 하려면 먼저 num까지 push 해야함
    while current <= num:
        stack.append(current)
        result.append('+')
        current += 1
    if stack[-1] != num:
        print("NO")
        exit(0)
    stack.pop()
    result.append('-')
print('\n'.join(result))