from collections import deque

def BFS(begin, target, words):
    answer = 0
    queue = deque([(begin, 0)])
    
    while queue:
        now, step = queue.popleft()
        
        if now == target :
            return step
        for word in words:
            cnt = 0
            print("오잉 " + word)
            for i in range(len(word)):
                if now[i] != word[i]:
                    cnt +=1
            if cnt == 1:
                queue.append((word, step+1))
            
def solution(begin, target, words):
    if target not in words:
        return 0
    
    return BFS(begin, target, words)
