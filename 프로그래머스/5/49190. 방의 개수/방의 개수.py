from collections import defaultdict

def solution(arrows):
    answer = 0
    N = len(arrows)
    dx = [-1,-1,0,1,1,1,0,-1]; dy = [0,1,1,1,0,-1,-1,-1]
    direction = {i:(dx[i],dy[i]) for i in range(8)}
    visited = defaultdict(list) # ((x,y)):[dir]
    
    x,y = 0,0
    visited[(x,y)]
    
    for d in arrows:
        dx,dy = direction[d]
        for i in range(2):
            new_x = x+dx; new_y = y+dy
            # if not (new_x,new_y) in visited:
            #     visited[(new_x,new_y)].append(d)
            if (new_x,new_y) in visited:
                if d in visited[(new_x,new_y)]:
                    pass
                elif (d+4)%8 in visited[(x,y)]:
                    pass
                else:
                    answer += 1
            visited[(new_x,new_y)].append(d)
            x,y = new_x,new_y
            
    return answer
    return answer