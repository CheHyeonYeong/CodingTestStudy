def solution(code):
    ret = ''
    mode = True # 0
    for idx in range(len(code)):
        if code[idx] == '1':
            mode = not mode
            continue
        else : 
            if mode and idx % 2 == 0:
                ret+=code[idx]
            elif not mode and idx % 2 == 1 :
                ret+= code[idx]

                    
    return ret if ret else "EMPTY"