from collections import deque

def solution(n, edge):
    answer = 0
    
    graph = [[] for _ in range(n+1)]
    for e0,e1 in edge:
        graph[e0].append(e1); graph[e1].append(e0)
    visited = [0 for _ in range(n+1)]
    
    def dfs(graph, v, visited):
        queue = deque()
        queue.append(v)
        visited[v]=1
        
        while queue:
            v = queue.popleft()
            for new_v in graph[v]:
                if not visited[new_v]:
                    visited[new_v] = visited[v]+1
                    queue.append(new_v)
                    
    dfs(graph, 1, visited)
    
    far = max(visited)              
    for v in visited:
        if v==far:
            answer += 1
            
    return answer