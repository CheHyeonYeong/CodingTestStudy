
while True:
    a = int(input())
    if a == 0:
        break
    a = list(str(a))
    b = [a[-i] for i in range(1, len(a) + 1)]
    print("yes" if a==b else "no")