def solution(a, b, c):
    answer = {a, b, c}
    
    if len(answer) ==3:
        return  a+b+c
    elif len(answer) == 2:
        return (a+b+c) * (a*a + b*b + c*c) 
    else:
        return (a+b+c) * (a*a + b*b + c*c) * (a*a*a + b*b*b + c*c*c)