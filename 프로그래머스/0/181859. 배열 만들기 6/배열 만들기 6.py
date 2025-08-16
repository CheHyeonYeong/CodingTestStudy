def solution(arr):
    if not arr : 
        return [-1]
    stk = []
    
    for i in arr:
        stk.pop() if stk and stk[-1] == i else stk.append(i) 
        
        
    return stk or [-1]