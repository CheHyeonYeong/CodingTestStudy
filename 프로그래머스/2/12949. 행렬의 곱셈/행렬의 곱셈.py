def solution(arr1, arr2):
    answer = [[0]* len(arr2[0]) for _ in range(len(arr1))]
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            total = 0
            for k in range(len(arr1[0])): # 중간 인덱스 (A의 열 = B의 행)
                total += arr1[i][k] * arr2[k][j]
            answer[i][j] = total
    return answer