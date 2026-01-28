
n = int(input())
meeting = []
for i in range(n):
    meeting.append(list(map(int, input().split())))
meeting.sort(key=lambda x: (x[1], x[0]))
et, cnt = 0,0

for x, y in meeting:
    if x>=et:
        et = y
        cnt += 1
print(cnt)