from collections import deque

def solution(maps):
    answer = 0
    N,M = len(maps), len(maps[0])
    x,y = 0,0
    
    def bfs(graph,v,visited):
        queue = deque()
        queue.append(v)
        x,y = v
        visited[x][y] = 1
        
        
        while queue:
            v = queue.popleft()
            x,y = v
            for dx,dy in [[-1,0],[1,0],[0,-1],[0,1]]:
                new_x = x+dx; new_y = y+dy
                if new_x<0 or new_y<0 or new_x>=N or new_y>=M:
                    continue
                elif new_x==N-1 and new_y==M-1:
                    return visited[x][y]+1
                if not visited[new_x][new_y] and graph[new_x][new_y]:
                    queue.append((new_x,new_y))
                    visited[new_x][new_y] = visited[x][y]+1
        return -1
    
    visited = [[0 for _ in range(M)] for _ in range(N)]
    answer = bfs(maps,(x,y),visited)
    
    return answer