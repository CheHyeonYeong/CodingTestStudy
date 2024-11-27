def solution(numbers):
    answer = []
    numbers.sort();
    # 모든 경우의 수 구함
    for i in range(len(numbers)) : 
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i]+numbers[j])
    # set으로 중복 없애도 정렬해서 반환
    return sorted(set(answer))
