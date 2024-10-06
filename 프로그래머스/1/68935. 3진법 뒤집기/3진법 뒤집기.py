def goToThree(n):
    num = []
    while n > 0:
        num.append(n % 3)
        n //= 3
    return num

def goToTen(n):
    num = 0
    n.reverse()
    for i in range(len(n)):
        num += 3**i * n[i]
    return num

def solution(n):
    return goToTen(goToThree(n))