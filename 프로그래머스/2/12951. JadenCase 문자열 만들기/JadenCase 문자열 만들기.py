def solution(s):
    # 문자열을 공백을 기준으로 나누되, 연속된 공백도 유지
    words = s.split(' ')
    
    jaden_words = []
    for word in words:
        if word:
            # 첫 글자를 대문자로, 나머지는 소문자로 변환
            jaden_word = word[0].upper() + word[1:].lower()
            jaden_words.append(jaden_word)
        else:
            # 빈 문자열(연속된 공백)은 그대로 추가
            jaden_words.append(word)
    
    # 변환된 단어들을 다시 공백으로 연결
    return ' '.join(jaden_words)
