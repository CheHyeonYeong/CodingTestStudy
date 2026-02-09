
n,x = map(int, input().split())
numbers = list(map(int, input().split()))

answer = [i for i in numbers if i < x]
print(' '.join(map(str, answer)))
