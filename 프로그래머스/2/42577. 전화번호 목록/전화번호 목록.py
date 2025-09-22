def solution(phone_book):
    hMap = {}
    for i in phone_book:
        hMap[i] = 1
    for number in phone_book:
        temp = ""
        for char in number[:-1]:
            temp+=char
            if temp in hMap:
                return False
    return True
