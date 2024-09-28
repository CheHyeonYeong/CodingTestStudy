def solution(sizes):
    sizes = [sorted(size, reverse=True) for size in sizes]
    
    max_first = max(size[0] for size in sizes)
    max_second = max(size[1] for size in sizes)
    return max_first * max_second