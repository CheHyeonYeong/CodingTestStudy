def solution(arr, k):
    # 중복 제거 + 순서 유지
    seen = set()
    answer = []
    for x in arr:
        if x not in seen:
            seen.add(x)
            answer.append(x)

    # 길이 맞추기
    if len(answer) >= k:
        return answer[:k]
    else:
        return answer + [-1] * (k - len(answer))
