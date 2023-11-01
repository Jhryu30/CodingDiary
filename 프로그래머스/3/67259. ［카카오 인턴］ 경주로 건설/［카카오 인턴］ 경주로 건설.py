from collections import deque

def solution(board):
    answer = 0
    N = len(board)
    dir_dict = {0:[-1,0], 1:[1,0], 2:[0,-1], 3:[0,1]}
    
    def bfs(graph,v,visited):
        nonlocal dir_dict
        queue = deque()
        queue.append(v)
        
        while queue:
            x,y,d = queue.popleft()
            for new_d in range(4):
                dx,dy = dir_dict[new_d]
                new_x = x+dx; new_y = y+dy
                cost = 100 if new_d==d else 600
                if not visited[x][y][d]: cost = 100
                
                if new_x<0 or new_y<0 or new_x>=N or new_y>=N:
                    continue
                elif not graph[new_x][new_y]:
                    if not visited[new_x][new_y][new_d] or visited[new_x][new_y][new_d]>visited[x][y][d]+cost:
                        visited[new_x][new_y][new_d] = visited[x][y][d]+cost
                        queue.append([new_x,new_y,new_d])
                        
        return visited[N-1][N-1]
    
    visited = [[[0,0,0,0] for _ in range(N)] for _ in range(N)]
    bfs(board, [0,0,0], visited)
    answer = min([v for v in visited[N-1][N-1] if v>0])
    
    return answer