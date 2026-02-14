import sys
input = sys.stdin.readline

from collections import Counter

n = int(input())

numbers = []
for _ in range(n):
    numbers.append(int(input()))

numbers.sort()
counter = Counter(numbers)
max_counter = max(counter.values())
mode_list = [num for num, cnt in counter.items() if cnt == max_counter]

print(round(sum(numbers)/n))
print(numbers[n//2])
if len(mode_list) > 1:
    print(mode_list[1])
else:
    print(mode_list[0])
print(numbers[-1]-numbers[0])
