from collections import deque

def solution(land):
    answer = 0
    n,m = len(land),len(land[0])
    visited = [[0 for _ in range(m)] for _ in range(n)]
    
    def bfs(graph,v,visted):
        queue = deque()
        queue.append(v)
        x,y = v
        min_y,max_y,cnt = y,y,1
        visited[x][y] = 1
        
        while queue:
            x,y = queue.popleft()
            for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                new_x, new_y = x+dx, y+dy
                if new_x<0 or new_y<0 or new_x>=n or new_y>=m:
                    continue
                if not visited[new_x][new_y] and graph[new_x][new_y]:
                    visited[new_x][new_y] = 1
                    queue.append((new_x,new_y))
                    min_y,max_y = min(new_y,min_y),max(new_y,max_y)
                    cnt += 1
                    
        return min_y,max_y,cnt
    
    oil = [0 for _ in range(m)]
    for x in range(n):
        for y in range(m):
            if not visited[x][y] and land[x][y]:
                min_y,max_y,cnt = bfs(land,(x,y),visited)
                for oil_y in range(min_y,max_y+1):
                    oil[oil_y] += cnt
                    
    answer = max(oil)
    
    return answer