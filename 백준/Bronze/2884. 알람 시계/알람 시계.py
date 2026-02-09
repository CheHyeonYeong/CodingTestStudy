h,m = map(int, input().split())

# 45분전으로 진행..
if h == 0 and m < 45:
    print("23 "+str(15+m))
elif m < 45:
    print(str(h-1)+" "+str(15+m))
else:
    print(str(h) +" "+str(m-45))