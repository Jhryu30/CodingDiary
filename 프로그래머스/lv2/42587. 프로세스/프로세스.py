from collections import deque

def solution(priorities, location):
    answer = 0
    
    queue = deque([p,0] for p in priorities)
    queue[location][1] = 1
    
    max_p = list(reversed(sorted(priorities)))
    
    while queue:
        current = queue.popleft()
        if current[0] == max_p[answer]:
            answer += 1
            if current[1]:
                return answer
        else:
            queue.append(current)
            
    return answer