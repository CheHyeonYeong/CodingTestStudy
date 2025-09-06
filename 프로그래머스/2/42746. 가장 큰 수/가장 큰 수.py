def solution(numbers):
    answer = ''
    numlist = list(map(str, numbers))
    numlist.sort(key = lambda x: x*3, reverse = True)
    for i in numlist:
        answer += i
        
    return str( int(answer))