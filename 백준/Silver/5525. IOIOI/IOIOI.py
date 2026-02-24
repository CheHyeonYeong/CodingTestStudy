n = int(input())      # 우리가 찾을 패턴의 N (P_n = I(OI)^n)
m = int(input())      # 문자열 길이 (사실 len(s)와 같음)
s = input().strip()   # 전체 문자열

count = 0   # 연속된 "IOI" 패턴 개수
answer = 0  # 최종적으로 찾은 P_n 개수
i = 1       # 가운데 문자부터 탐색 (i-1, i, i+1을 보기 위해 1부터 시작)

while i < m - 1:  # i+1까지 봐야 하므로 m-1까지만 반복
    # 현재 위치를 기준으로 앞뒤 포함 3글자가 "IOI"인지 확인
    if s[i-1:i+2] == "IOI":
        count += 1  # 연속된 IOI 개수 증가
        
        # IOI가 n번 이상 연속되면 P_n 완성
        if count >= n:
            answer += 1  # 하나 발견
        
        # IOI는 "I O I" 형태라서
        # 다음 후보는 2칸 뒤부터 보면 됨 (중복 계산 방지)
        i += 2
    else:
        # 패턴이 끊기면 연속 카운트 초기화
        count = 0
        i += 1  # 한 칸씩 이동

print(answer)