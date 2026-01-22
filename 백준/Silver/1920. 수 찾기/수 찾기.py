
n = int(input())
nArr = list(map(int, input().split()))
m = int(input())
mArr = list(map(int, input().split()))
findArr = set(nArr)

resultList = [0] * m
for i in range(m):
    if mArr[i] in findArr:
        resultList[i] = 1

for i in resultList:
    print(i)