
n, k = map(int, input().split())

number = input().strip()
answer = []
remove_count = 0

for digit in number:
    while answer and remove_count < k and answer[-1]< digit:
        answer.pop()
        remove_count += 1
    answer.append(digit)

answer = answer[:n-k]
print(''.join(answer))