
n = int(input())
string = list()
for _ in range(n):
    string.append(input().strip())
string = list(set(string))
string.sort(key = lambda x : (len(x),x))

print("\n".join(string))