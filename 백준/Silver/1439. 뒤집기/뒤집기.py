
s = input()
group0 = len([x for x in s.split("0") if x != ''])
group1 = len([x for x in s.split("1") if x != ''])
print(min(group0, group1))