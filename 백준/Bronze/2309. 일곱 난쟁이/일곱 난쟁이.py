
key = [0] * 9
for i in range(9):
    key[i] = int(input())

minus = sum(key) - 100
flag, a,b = False, 0,0

for i in range(9):
    for j in range(i + 1, 9):
        if minus == key[i] + key[j]:
            flag, a,b = True,i,j
            break
    if flag:
        break
key.pop(b)
key.pop(a)

key.sort()

for i in range(len(key)):
    print(key[i])