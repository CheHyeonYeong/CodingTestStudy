
n,m = map(int, input().strip().split())
cards = list(map(int, input().strip().split()))

cards.sort(reverse=True)
answer = 0
for i in range(n):
    for j in range(i+1, n-1):
        for k in range(j+1,n):
            if cards[i] + cards[j] + cards[k] > m:
                continue
            else:
                answer = max(answer, cards[i]+ cards[j]+ cards[k] )
print(answer)