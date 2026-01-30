def solution(str):
    stack = []
    flag = True
    mapping = {
        ")" : "("
    }
    
    for s in str:
        if s in mapping.values():
            stack.append(s)
        else:
            if not stack or stack[-1] != mapping[s]:
                flag = False
                break
            stack.pop()
    if stack: flag = False
    
    return flag