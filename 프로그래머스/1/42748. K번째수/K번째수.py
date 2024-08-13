def solution(array, commands):
    answer = []
    result = []
    for i,j,k in commands:
        #answer.append(sorted(array[i-1:j])[k-1])

        result = sorted(array[i-1:j])
        answer.append(result[k-1])
    return answer