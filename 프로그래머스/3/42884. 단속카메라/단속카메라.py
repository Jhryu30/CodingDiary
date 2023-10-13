from collections import deque

def solution(routes):
    answer = 1
    routes.sort(key=lambda x: (x[0],x[1]))
    
    queue = deque(routes)
    x0,y0 = queue.popleft()
    flag = y0
    
    while queue:
        x1,y1 = queue.popleft()
        if x1<=flag:
            # 겹치는 구간이 있는 경우
            if flag>y1:
                # 이전 구간에 속하는 경우
                flag = y1
        else:
            # 겹치는 구간이 없는 경우
            flag = y1
            answer += 1
            queue.appendleft([x1,y1])
        x0,y0 = x1,y1
        
    return answer