
results = []
while True:
    dic = {")":"(", "]":"["}

    result = input()
    if result == '.':
        break

    stack = []
    valid = True
    for s in result:
        if s in dic.values():
            stack.append(s)
        elif s in dic.keys():
            if stack and stack[-1] == dic[s]:
                stack.pop()
            else:
                valid = False
                break
    if not valid or stack:
        print("no")
    else:
        print("yes")
