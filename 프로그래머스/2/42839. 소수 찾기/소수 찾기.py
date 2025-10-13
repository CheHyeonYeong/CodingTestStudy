def isPrime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    else:
        for i in range(3, int(num**0.5)+1, 2):
            if num%i == 0:
                return False 
        else:
            return True
def DFS(currentNum, nums, ch, resultSet):
    if currentNum > 0 :
        resultSet.add(currentNum)
    for i in range(len(nums)):
        if ch[i] == 0:
            ch[i] = 1
            DFS(currentNum * 10 + nums[i], nums, ch, resultSet)
            ch[i]=0
def solution(numbers):
    nums = [int(digit) for digit in numbers]
    resultSet = set()
    
    ch = [0] * len(nums)
    
    answer = 0
    DFS(0, nums, ch, resultSet)
    for i in resultSet:
        if isPrime(i):
            answer+=1
    return answer