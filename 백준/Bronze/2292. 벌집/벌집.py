
n = int(input())

count = 0
total = 1
spot = 6
# 1-> 2~7(6)->8~19 (12) ->20~37(18)

while total < n:
    total += spot
    spot += 6
    count += 1

print(count+1)