
n,s = map(int, input().split())
nums = list(map(int, input().split()))
cnt = 0
def DFS(L, sum):
    global cnt
    if L == n:
        if sum == s:
            cnt += 1
        return
    else:
        DFS(L+1, sum + nums[L])
        DFS(L+1, sum )

DFS(0, 0)
if s == 0 :
    cnt -= 1
print(cnt)