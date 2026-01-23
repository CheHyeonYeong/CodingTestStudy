
str = input()
alpha = [0]*26
for c in str:
    alpha[ord(c)-97] +=1

for i in alpha:
    print(i, end = " ")