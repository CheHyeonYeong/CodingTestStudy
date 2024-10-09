def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        combined = arr1[i]|arr2[i]
        binary = bin(combined)
        binary = binary[2:]
        binary = binary.zfill(n)        
        decoded = ""
        for bit in binary :
            if bit == '1':
                decoded += '#'
            else : 
                decoded += ' '
        answer.append(decoded)
    return answer