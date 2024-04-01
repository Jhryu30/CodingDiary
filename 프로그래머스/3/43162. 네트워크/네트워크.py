from collections import defaultdict, deque

def solution(n, computers):
    answer = 0
    
    graph = defaultdict(list)
    for i in range(n):
        for j in range(n):
            if computers[i][j]:
                graph[i].append(j)
                graph[j].append(i)
                
    def bfs(graph,v,visited):
        nonlocal answer
        queue = deque()
        queue.append(v)
        visited[v] = 1
        
        while queue:
            v = queue.popleft()
            for new_v in graph[v]:
                if not visited[new_v]:
                    visited[new_v] = 1
                    queue.append(new_v)
        answer += 1
        
    visited = [0 for _ in range(n)]
    for i in range(n):
        if not visited[i]:
            bfs(graph,i,visited)
    
    return answer