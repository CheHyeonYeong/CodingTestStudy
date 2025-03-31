def solution(a, b):
    answer = 0
    return int(str(a)+str(b)) if str(a)+str(b) > str(b)+str(a) else int(str(b)+str(a) )