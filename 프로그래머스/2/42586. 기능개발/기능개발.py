def solution(progresses, speeds):
    answer = []
    days_left = []  # 각 작업의 남은 일수를 저장할 리스트
    
    # 1. 진도에 따른 남은 일수 계산
    for progress, speed in zip(progresses, speeds):
        days = (100 - progress) // speed  # 남은 일수 계산
        if (100 - progress) % speed != 0:
            days += 1
        days_left.append(days)  # 계산된 남은 일수를 리스트에 추가
    
    # 2. 배포 일정 확인
    while days_left:
        count = 1
        first_day = days_left.pop(0)  # 첫 번째 작업의 남은 일수
        
        # 남은 작업들 중 첫 번째 작업보다 먼저 완료되는 작업 확인
        while days_left and days_left[0] <= first_day: # 그 다음날 배포가 되기 때문
            days_left.pop(0)
            count += 1
        
        # 함께 배포되는 작업 수를 결과 리스트에 추가
        answer.append(count)
    
    return answer