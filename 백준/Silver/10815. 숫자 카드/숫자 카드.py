n = int(input())
nums = set(map(int, input().split()))
m = int(input())
m_nums = list(map(int, input().split()))

for i in m_nums:
    if i in nums:
        print(1, end=" ")
    else :
        print(0, end=" ")