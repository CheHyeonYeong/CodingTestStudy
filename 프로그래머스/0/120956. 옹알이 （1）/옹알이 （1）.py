def solution(babbling):
    answer = 0
    baby = ["aya", "ye", "woo", "ma" ]
    
    for i in babbling:
        for j in range(4):
            if baby[j] in i:
                i = i.replace(baby[j]," ")
        i = i.replace(" ","")
        if len(i) == 0:
            answer += 1
    return answer