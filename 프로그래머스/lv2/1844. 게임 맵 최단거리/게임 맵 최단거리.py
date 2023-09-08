from collections import deque

def solution(maps):
    answer = 0
    global N, M
    N = len(maps); M = len(maps[0])
    visited = [[0 for _ in range(M)] for _ in range(N)]
    answer = bfs(maps, (0,0), visited)
    return answer

def bfs(graph, v, visited):
    x,y = v
    queue = deque()
    queue.append((x,y))
    visited[x][y] = 1
    
    while queue:
        x,y = queue.popleft()
        
        for dx,dy in [[-1,0],[1,0],[0,-1],[0,1]]:
            new_x = x+dx; new_y = y+dy
            if new_x<0 or new_x>=N or new_y<0 or new_y>=M:
                continue
            elif new_x==N-1 and new_y==M-1:
                return visited[x][y]+1
            elif graph[new_x][new_y]==1 and not visited[new_x][new_y]:
                visited[new_x][new_y] = visited[x][y]+1
                queue.append((new_x,new_y))
                
    return -1