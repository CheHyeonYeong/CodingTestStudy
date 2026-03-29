
import sys
input = sys.stdin.readline

T = int(input())
nums = list(map(int, input().split()))
target = int(input())
nums.sort()
l = 0
r = T -1
answer = 0

while l < r:
    csum = nums[l] + nums[r]
    if csum == target:
        answer += 1
        l += 1
        r -= 1
    elif csum < target:
        l += 1
    else:
        r -= 1

print(answer)