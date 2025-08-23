def solution(ineq, eq, n, m):
    if n>m:
        return 1 if ineq == ">" else 0
    elif n<m:
        return 1 if ineq == "<" else 0
    else:
        return 1 if eq == "=" else 0
    