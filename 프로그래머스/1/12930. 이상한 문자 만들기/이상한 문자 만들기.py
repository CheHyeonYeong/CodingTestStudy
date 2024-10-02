def solution(s):
    words = s.split(' ')
    result = []
    for word in words:
        if word:
            new_word = ''.join([c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(word)])
            result.append(new_word)
        else:
            result.append('')
    return ' '.join(result)