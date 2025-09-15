def solution(number, k):
    answer = []
    for num in number:
        num = int(num)
        while answer and k>0 and answer[-1] < num:
            answer.pop()
            k-=1
        answer.append(num)
    if k != 0:
        answer = answer[:-k]
    
    return ''.join(map(str, answer))