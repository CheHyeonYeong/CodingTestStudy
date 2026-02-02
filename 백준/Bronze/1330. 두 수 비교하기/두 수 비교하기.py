
a,b = map(int, input().split())
dict = {
    1:">",
    -1:"<",
    0:"=="
}
if a-b == 0: print(dict[0])
elif a-b<0:
    print(dict[-1])
else:
    print(dict[1])