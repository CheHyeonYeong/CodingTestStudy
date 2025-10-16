def solution(brown, yellow):
    total = brown + yellow
    for i in range(3, total//2):
        j = total // i
        if i*j == total and (i-2) * (j-2) == yellow:
            return [j,i]