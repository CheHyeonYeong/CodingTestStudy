import sys
from io import StringIO
from math import inf
# ========== 로컬 테스트용 ==========
# 제출 전에 아래 3줄 주석처리!
test_input = open("input.txt").read()
sys.stdin = StringIO(test_input)
# ==================================
import sys
input = sys.stdin.readline

T = int(input())
nums = list(map(int, input().split()))
nums.sort()

l = 0
r = T -1
result = inf
answer = [0,0]
while l < r:
    csum = nums[l] + nums[r]
    if abs(csum) < result:
        result = abs(csum)
        answer[0] = nums[l]
        answer[1] = nums[r]

    if csum < 0:
        l += 1
    else:
        r -= 1
print("{0} {1}".format(answer[0], answer[1]))