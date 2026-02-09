
n = int(input())
for _ in range(n):
    string = input().strip()
    count = 0
    answer = []
    for c in string:
        if c == 'X':
            answer = []
        else:
            answer.append(c)
            count += len(answer)
    print(count)