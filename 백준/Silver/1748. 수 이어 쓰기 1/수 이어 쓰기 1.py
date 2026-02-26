
n = input()
l = len(n)
n = int(n)
ans = 0
for i in range(1, l):
    ans += i * (9 * (10 **(i-1)))

ans += (n - 10 **(l-1) + 1) *l
print(ans)