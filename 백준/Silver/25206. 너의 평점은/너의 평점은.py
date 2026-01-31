import sys
dic = {
"A+":	4.5,
"A0":	4.0,
"B+":	3.5,
"B0":	3.0,
"C+":	2.5,
"C0":	2.0,
"D+":	1.5,
"D0":	1.0,
"F":	0.0
}
answer = 0.0
cnt = 0
for _ in range(20):
    k, n, score = sys.stdin.readline().split()
    if score in dic:
        answer += float(n) * dic[score]
        cnt += float(n)
    else:
        continue

print( 0 if answer == 0.0 else answer/cnt )