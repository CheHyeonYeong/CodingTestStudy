def solution(arr):
    if not arr : 
        return [-1]
    
    stk, i = [], 0
    
    for i in arr:
        stk.pop() if stk and stk[-1] == i else stk.append(i) 
        
        
    return [-1] if len(stk) == 0 else stk