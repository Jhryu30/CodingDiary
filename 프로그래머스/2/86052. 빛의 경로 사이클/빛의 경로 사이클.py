from collections import defaultdict

def solution(grid):
    answer = []
    n,m = len(grid),len(grid[0])
    dir_dict = {0:(0,1),1:(1,0),2:(0,-1),3:(-1,0)}
    answer_dict = defaultdict(list)
    visited = [[[0,0,0,0] for _ in range(m)] for _ in range(n)]
    
    for x in range(n):
        for y in range(m):
            for d in range(4):
                cnt = 1
                while not visited[x][y][d]:
                    visited[x][y][d] = 1

                    if grid[x][y]=="S":
                        pass
                    elif grid[x][y]=="L":
                        d = (d-1)%4
                    else:
                        d = (d+1)%4

                    dx,dy = dir_dict[d]
                    x,y = (x+dx)%n,(y+dy)%m
                    cnt+=1
                
                if cnt>1:
                    answer.append(cnt-1)
                # if not visited in answer_dict[cnt-1]:
                #     answer_dict[cnt-1].append(visited)
                #     answer.append(cnt-1)
            
    return sorted(answer)