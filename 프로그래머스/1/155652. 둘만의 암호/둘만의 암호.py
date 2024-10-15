def solution(s, skip, index):
    answer = ''
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    for char in s:
        current_index = alphabet.index(char)
        count = 0
        while count < index:
            current_index = (current_index + 1) % 26
            if alphabet[current_index] not in skip:
                count += 1
        answer += alphabet[current_index]
    
    return answer