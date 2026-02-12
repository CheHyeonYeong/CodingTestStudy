
n = int(input())

stack = []
for _ in range(n):
    k = int(input())
    if k != 0:
        stack.append(k)
    else:
        stack.pop()

print(sum(stack))