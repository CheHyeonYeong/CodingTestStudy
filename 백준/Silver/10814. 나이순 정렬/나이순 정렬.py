
n = int(input())
people = []
for i in range(n):
    people.append(input().strip().split())
    people[i][0] = int(people[i][0])
    people[i].append(i)

people.sort(key = lambda x: (x[0], x[2]))

for person in people:
    print(str(person[0])+" "+person[1])