from collections import deque

def solution(people, limit):
    answer,N = 0, len(people)
    queue = deque(sorted(people))
    
    while queue:
        boat,cnt = 0, 0
        while queue and boat+queue[-1]<=limit and cnt<2:
            boat += queue.pop()
            cnt += 1
        while queue and boat+queue[0]<=limit and cnt<2:
            boat += queue.popleft()
            cnt += 1
        answer += 1
        
    return answer