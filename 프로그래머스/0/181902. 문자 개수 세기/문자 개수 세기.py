def solution(my_string):
    answer = [0] * 52
    for i in my_string:
        o = ord(i)
        answer[o - 65 if o < 97 else o - 71] += 1

    return answer