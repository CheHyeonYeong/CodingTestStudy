
S = list(input().strip())
T = list(input().strip())

result = []
while True:
    if T == S:
        result.append("1")
        break
    if len(T) == 0 :
        break
    if T[-1] == "A":
        T = T[:-1]
        continue
    if T[-1] == "B":
        T = T[:-1][::-1]
        continue
# 아니면 0을 출력한다
if not result :
    result.append("0")
print("".join(result))