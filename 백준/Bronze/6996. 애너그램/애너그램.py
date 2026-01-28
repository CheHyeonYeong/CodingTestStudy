
T = int(input())
answer = [0]*T
for i in range(T):
    answer[i] = input().split()

for i in range(T):
    if len(answer[i][0]) != len(answer[i][1]):
        print("{0} & {1} are NOT anagrams.".format(answer[i][0], answer[i][1]))
        continue
    if sorted(answer[i][0]) == sorted(answer[i][1]):
        print("{0} & {1} are anagrams.".format(answer[i][0], answer[i][1]))
    else :
        print("{0} & {1} are NOT anagrams.".format(answer[i][0], answer[i][1]))