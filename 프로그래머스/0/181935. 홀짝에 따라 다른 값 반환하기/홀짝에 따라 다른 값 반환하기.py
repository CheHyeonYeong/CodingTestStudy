def solution(n):
    answer = 0
    if(n%2==1):
        answer = (n//2+1)*(1+n) //2
    else : 
        answer = 4*(n//2)*(n//2+1)*(n+1)//6
    return answer