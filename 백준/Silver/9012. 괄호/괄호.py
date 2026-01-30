
n = int(input())

for i in range(n):
    str = input()
    stack = []
    flag = True
    for s in str:
        if s == '(':
            stack.append(s)
        elif s == ')':
            if not stack:
                flag = False
                break
            stack.pop()
    if stack: flag = False
    print("YES" if flag else "NO")
