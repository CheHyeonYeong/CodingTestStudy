def solution(friends, gifts):
    answer = 0
    count = len(friends)
    # 선물지수
    dic = {}
    for i in friends:
        dic[i] = 0
    
    # 주고받은 선물 : [준사람][받은사람]
    gift = [[0] * count for _ in range(count)] 
    
    for i in gifts:      
        a,b = i.split(" ")
        dic[a] += 1
        dic[b] -= 1
        gift[friends.index(a)][friends.index(b)] += 1
    next_month = [0] * count

    # 모든 친구 쌍 비교 (i < j 조건으로 중복 방지)
    for i in range(count):
        for j in range(i + 1, count):  # i+1부터 시작해서 중복 비교 방지
            # i와 j 사이의 선물 교환 규칙 적용
            give_i_to_j = gift[i][j]  # i가 j에게 준 선물 수
            give_j_to_i = gift[j][i]  # j가 i에게 준 선물 수

            if give_i_to_j > give_j_to_i:
                # i가 j보다 더 많이 줬으면 i가 선물 받음
                next_month[i] += 1
            elif give_i_to_j < give_j_to_i:
                # j가 i보다 더 많이 줬으면 j가 선물 받음
                next_month[j] += 1
            else:
                # 주고받은 수가 같으면 선물 지수 비교
                gift_index_i = dic[friends[i]]
                gift_index_j = dic[friends[j]]

                if gift_index_i > gift_index_j:
                    # i의 선물 지수가 더 높으면 i가 선물 받음
                    next_month[i] += 1
                elif gift_index_i < gift_index_j:
                    # j의 선물 지수가 더 높으면 j가 선물 받음
                    next_month[j] += 1
                # 선물 지수도 같으면 아무도 선물 못 받음 (else 생략)

    answer = max(next_month)
    
    return answer