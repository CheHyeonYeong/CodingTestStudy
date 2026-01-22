import sys
from io import StringIO

# ========== 로컬 테스트용 ==========
# 제출 전에 아래 3줄 주석처리!
test_input = open("input.txt").read()
sys.stdin = StringIO(test_input)
# ==================================

input = sys.stdin.readline

# 풀이 시작
n = int(input())
arr = list(map(int, input().split()))

print(sum(arr))
