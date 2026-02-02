numbers = []
for _ in range(9):
    numbers.append(int(input()))

num = list(enumerate(numbers))
num = sorted(num, key=lambda x: x[1], reverse=True)

print(num[0][1])
print(num[0][0]+1)