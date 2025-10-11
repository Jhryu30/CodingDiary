def solution(n, m, x, y, queries):
    x1,x2,y1,y2 = x,x,y,y
    
    while queries:
        query = queries.pop()
        cmd,d = query
        if cmd==0: # -dy -> +dy
            y2 = min(m-1, y2+d)
            if y1>0:
                y1 += d
                if y1>m-1:
                    return 0
            
        if cmd==1: # +dy -> -dy
            y1 = max(0, y1-d)
            if y2<m-1:
                y2 -= d
                if y2<0:
                    return 0
                
        if cmd==2: # -dx -> +dx
            x2 = min(n-1, x2+d)
            if x1>0:
                x1 += d
                if x1>n-1:
                    return 0

        if cmd==3: # +dx -> -dy
            x1 = max(0, x1-d)
            if x2<n-1:
                x2 -= d
                if x2<0:
                    return 0
            
    answer = (x2-x1+1)  * (y2-y1+1)
    return answer
