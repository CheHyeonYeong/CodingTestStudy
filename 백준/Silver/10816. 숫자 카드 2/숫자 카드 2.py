n = int(input())
numbers= list(map(int, input().split()))
m= int(input())
mumber = list(map(int, input().split()))
dic = {}
for i in range(m):
    dic[mumber[i]] = 0

for i in range(n):
    if numbers[i] in dic:
        dic[numbers[i]] += 1
result = []
for i in range(m):
    result.append(dic[mumber[i]])

print(" ".join(map(str, result)))