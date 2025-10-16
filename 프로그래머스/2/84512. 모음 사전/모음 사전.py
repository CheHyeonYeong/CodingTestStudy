def solution(word):
    answer = 0
    alpha = {'A':0, 'E':1, 'I':2,'O':3,'U':4}
    number = [781, 156,31,6,1]
    for i in range(len(word)):
        answer +=  alpha[word[i]] * number[i] + 1
    return answer