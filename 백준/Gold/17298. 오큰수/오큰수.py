
n = int(input())
A = list(map(int, input().split()))
result = [-1]*n
stack = []
for i in range(n):
    # 현재 값이 스택top의 값보다 크면, 스택 top의 오큰수는 현재값
    while stack and A[stack[-1]] < A[i]:
        result[stack.pop()] =A[i]
    stack.append(i)

print(*result)