def solution(numbers):
    answer = set()
    numbers.sort();
    for i in range(len(numbers)) : 
        for j in range(i+1, len(numbers)):
            num = numbers[i]+numbers[j]
            answer.add(num)
    return sorted(list(answer))