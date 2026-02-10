
isbn = input().strip()
answer = 0
nt = 0
for i in range(len(isbn)):
    if isbn[i].isdigit():
        if i % 2 ==0:
            answer += int(isbn[i])
        else:
            answer += int(isbn[i]) * 3
    else:
        nt = 1 if i % 2 == 0 else 3
answer = 10 - (answer % 10)
need = answer %10
if nt == 1:
    print(need)
else:
    print(need * 7 %10)