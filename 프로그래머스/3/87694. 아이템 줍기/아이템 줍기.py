from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    N = len(rectangle)
    X_max,Y_max = 2*max([rectangle[i][2] for i in range(N)]), 2*max([rectangle[i][3] for i in range(N)])
    region = [[0 for _ in range(Y_max+1)] for _ in range(X_max+1)]
    for x1,y1,x2,y2 in rectangle:
        for x in range(2*x1,2*x2+1):
            for y in range(2*y1,2*y2+1):
                region[x][y] = 1
    for x1,y1,x2,y2 in rectangle:
        for x in range(2*x1+1,2*x2):
            for y in range(2*y1+1,2*y2):
                region[x][y] = 0
                
    def bfs(graph,v,visited):
        nonlocal X_max, Y_max
        queue = deque()
        queue.append(v)
        x,y = v
        visited[x][y] = 1
        
        while queue:
            x,y = queue.popleft()
            for dx,dy in [[-1,0],[1,0],[0,-1],[0,1]]:
                new_x = x+dx; new_y = y+dy
                if new_x<0 or new_y<0 or new_x>X_max or new_y>Y_max:
                    continue
                elif new_x==2*itemX and new_y==2*itemY:
                    return visited[x][y]//2
                elif not visited[new_x][new_y] and graph[new_x][new_y]:
                    visited[new_x][new_y] = visited[x][y]+1
                    queue.append((new_x,new_y))
                    
        return
    
    visited = [[0 for _ in range(Y_max+1)] for _ in range(X_max+1)]
    answer = bfs(region,(2*characterX,2*characterY),visited)
    
    return answer