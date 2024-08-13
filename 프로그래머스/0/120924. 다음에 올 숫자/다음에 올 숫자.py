def solution(common):
    a,d= common[0], common[1]-common[0]
    if a+2*d==common[2]:
        return a+len(common)*d
    else:
        r= common[1]//common[0]
        return a*r**(len(common))