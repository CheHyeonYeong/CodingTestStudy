def solution(numbers):
    num = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine" ]
    num1,answer='',''
    for i in numbers:
        num1+=i
        if num1 in num:
            answer+=str(num.index(num1))
            num1=''
    return int(answer)