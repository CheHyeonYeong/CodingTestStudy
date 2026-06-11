def solution(progresses, speeds):
    answer = []
    days = []
    
    for x,y in zip(progresses, speeds):
        day = (100-x) // y
        if (100-x) % y != 0:
            day += 1
        days.append(day)
    
    current_day = days[0]
    count = 0
    for day in days:
        if day <= current_day: 
            count +=1
        else:
            answer.append(count)
            current_day = day
            count = 1
        
    answer.append(count)
    
    return answer