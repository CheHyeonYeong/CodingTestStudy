def solution(arr):
    answer = []
    if 2 not in arr:
        answer.append(-1)
        return answer
    startindex = arr.index(2)
    end = len(arr)-1
    while(end>=0):
        if arr[end]==2:
            break
        else :
            end-=1

    return arr[startindex:end+1]
