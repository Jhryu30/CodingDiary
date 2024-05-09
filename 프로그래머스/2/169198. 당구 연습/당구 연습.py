def solution(m, n, startX, startY, balls):
    answer = []
    goal = {0:(-startX,startY), 1:(startX,-startY), 2:(2*m-startX,startY),3:(startX,2*n-startY)}
    
    for x,y in balls:
        no = 4
        if x==startX:
            no = 1 if y<startY else 3
        elif y==startY:
            no = 0 if x<startX else 2
        
        ans = []
        direction = [i for i in range(4) if not i==no]
        for d in direction:
            gx,gy = goal[d]
            ans.append((gx-x)**2+(gy-y)**2)
        print([goal[d] for d in direction])
                
        answer.append(min(ans))
        
    return answer