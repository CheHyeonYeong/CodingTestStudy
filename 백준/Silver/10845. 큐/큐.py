n = int(input())

num = []
result = []
for i in range(n):
    s = input().split()
    if s[0] == 'push': num.append(int(s[1]))
    elif s[0] == 'pop': result.append(num.pop(0) if num else -1)
    elif s[0] == 'empty': result.append(0 if num else 1)
    elif s[0] == 'size': result.append(len(num))
    elif s[0] == 'front': result.append(num[0] if num else -1)
    elif s[0] == 'back': result.append(num[-1] if num else -1)

print('\n'.join(map(str, result)))