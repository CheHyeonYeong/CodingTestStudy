
n,k = map(int, input().strip().split())

people = [x for x in range(1,n+1)]
answer = []
i = 0

while len(answer) < n:
    i = (i+k-1) % len(people)
    answer.append(people.pop(i))

print("<" + ", ".join(map(str, answer)) + ">")
