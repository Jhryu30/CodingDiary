from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    
    global N; N = max([max(rec) for rec in rectangle])
    graph = [[0 for _ in range(2*N+1)] for _ in range(2*N+1)]
    
    for rec in rectangle:
        for row in range(2*rec[0],2*rec[2]+1):
            graph[row][2*rec[1]:2*rec[3]+1] = [1 for _ in range(2*rec[3]-2*rec[1]+1)]
    for rec in rectangle:
        for row in range(2*rec[0]+1,2*rec[2]):
            graph[row][2*rec[1]+1:2*rec[3]] = [0 for _ in range(2*rec[3]-2*rec[1]-1)]
    
    
    #print('\n'.join([''.join(map(str,graph[i])) for i in range(len(graph))]))
    # BFS
    visited = [[0 for _ in range(2*N+1)] for _ in range(2*N+1)]
    answer = bfs(graph, (2*characterX,2*characterY), visited, (2*itemX,2*itemY))
    
    return answer//2

def bfs(graph, v, visited, v_end):
    x,y = v
    itemX, itemY = v_end
    queue = deque()
    queue.append((x,y))
    visited[x][y] = 1
    
    while queue:
        x,y = queue.popleft()
        for dx,dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            new_x = x+dx; new_y = y+dy
            if new_x<0 or new_x>=2*N+1 or new_y<0 or new_y>=2*N+1:
                continue
            elif new_x==itemX and new_y==itemY:
                return visited[x][y]
            elif graph[new_x][new_y]==1 and not visited[new_x][new_y]:
                visited[new_x][new_y] = visited[x][y]+1
                queue.append((new_x,new_y))
                
    return
        