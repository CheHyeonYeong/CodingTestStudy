
'''def solution(num, total):
    #연속된 num의 수만큼 더해서 total이 나올 때까지 계산
    count=total
    while(True):
        answer=[]
        for i in range(num,0,-1):
            answer.append(count-i)
        if sum(answer)==total:
            break
        else:
            count-=1
    return answer
    # 통과는 하지만 시간복잡도에서 애먹어서 새로운 방향성 탐구
    '''
def solution(num, total):
    #등차수열을 이용하기
    count=total/num-num/2-0.5
    return [int(count +i) for i in range(1,num+1,1)]
    
