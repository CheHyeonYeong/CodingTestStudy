def solution(answers):
    answer = [0]*3
    length = len(answers)
    one = [1, 2, 3, 4, 5] * (length//5+1)
    two = [2, 1, 2, 3, 2, 4, 2, 5] * (length//8 +1)
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * (length//10+1)
    for i in range(length):
        if answers[i] == one[i]:
            answer[0]+=1
        if answers[i] == two[i]:
            answer[1]+=1
        if answers[i] == three[i]:
            answer[2]+=1
    maxInt = max(answer)
    result = []
    for i in enumerate(answer):
        if maxInt <= i[1]:
            maxInt = i[1]
            result.append(i[0]+1)
    return result