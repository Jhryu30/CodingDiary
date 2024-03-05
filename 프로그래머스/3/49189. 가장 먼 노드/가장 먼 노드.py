from collections import defaultdict, deque
def solution(n, edge):
    answer = 0
    
    visited = [0 for _ in range(n+1)]
    graph = defaultdict(list)
    for a,b in edge:
        graph[a].append(b); graph[b].append(a)
    
    def bfs():
        nonlocal graph, visited
        queue = deque()
        queue.append(1)
        visited[1] = 1
        
        while queue:
            v = queue.popleft()
            for new_v in graph[v]:
                if not visited[new_v]:
                    visited[new_v] = visited[v]+1
                    queue.append(new_v)
                    
    bfs()
    depth = max(visited)
    for v in range(1,n+1):
        if visited[v]==depth:
            answer += 1
            
    return answer