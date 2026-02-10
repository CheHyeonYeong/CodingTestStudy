import math

N = int(input())
numbers = list(map(int, input().strip().split()))

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

count = 0

for k in range(N):
    if is_prime(numbers[k]):
        count +=1

print(count)