from collections import deque

def solution(routes):
    answer = 0
    routes = deque(sorted(routes))
    
    flag = 0 # 0(new), 1(intersect)
    while routes:
        if not flag:
            start,end = routes.popleft()
            answer += 1
            flag = 1
        else:
            new_start,new_end = routes.popleft()
            if new_start<=end and new_end>=start:
                start = max(start,new_start)
                end = min(end,new_end)
                flag = 1
            else:
                routes.appendleft([new_start,new_end])
                flag = 0
                
    return answer