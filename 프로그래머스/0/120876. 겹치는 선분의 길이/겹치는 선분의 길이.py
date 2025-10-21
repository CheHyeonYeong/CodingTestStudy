def solution(lines):
    line_count = [0] * 201
    
    for start, end in lines:
        for i in range(start, end):
            line_count[i + 100] += 1
    
    answer = 0
    for count in line_count:
        if count >= 2:  
            answer += 1
    
    return answer