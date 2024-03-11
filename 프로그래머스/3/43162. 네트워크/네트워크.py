from collections import defaultdict, deque

def solution(n, computers):
    answer = 0
    N = len(computers)
    graph = defaultdict(list)
    for i in range(N):
        graph[i] = [j for j in range(N) if computers[i][j]]
    
    def bfs(v):
        nonlocal graph, visited
        queue = deque()
        queue.append(v)
        visited[v] = 1
        
        while queue:
            v = queue.popleft()
            for new_v in graph[v]:
                if not visited[new_v]:
                    queue.append(new_v)
                    visited[new_v] = 1
    
    visited = [0 for _ in range(N)]
    for node in range(N):
        if not visited[node]:
            bfs(node)
            answer += 1
    
            
    return answer