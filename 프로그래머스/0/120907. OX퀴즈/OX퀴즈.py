def solution(quiz):
    answer = []
    for i in quiz:
        j = i.split(" ")
        if j[1] == '-':
            answer.append("O" if int(j[0])-int(j[2]) == int(j[4]) else "X")
        else : 
            answer.append("O" if int(j[0])+int(j[2]) == int(j[4]) else "X")
    return answer