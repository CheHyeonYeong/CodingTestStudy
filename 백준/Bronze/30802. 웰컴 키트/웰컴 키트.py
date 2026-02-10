N = int(input())
sizes = list(map(int, input().strip().split()))
T,P = map(int, input().split())

# 첫 줄 티셔츠 T장씩 최소 몇 묶음
# 펜을 P개씩 몇 묶음 + 1개씩 몇 개
answerT = 0
for i in sizes:
    if i == 0:
        continue
    if i<T:
        answerT +=1
    elif i % T == 0:
        answerT +=  i// T
    else :
        answerT += i // T + 1
print(str(answerT) + "\n"+ str(N//P)+" "+str(N%P))