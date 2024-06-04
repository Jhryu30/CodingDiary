from collections import defaultdict, deque

def solution(n, roads, sources, destination):
    graph = defaultdict(list)
    for a,b in roads:
        graph[a].append(b)
        graph[b].append(a)
    
    answer = []
    visited = [-1 for _ in range(n+1)]
    
    queue = deque([destination])
    visited[destination] = 0
    while queue:
        v = queue.popleft()
        for new_v in graph[v]:
            if visited[new_v]<0:
                queue.append(new_v)
                visited[new_v] = visited[v]+1
                
    answer = [visited[v] for v in sources]
    
    
    return answer