from collections import defaultdict, deque

def solution(n, results):
    answer = 0
    
    competition = defaultdict(list)
    for a,b in results:
        competition[a].append(b)
        
    def bfs(node,visited):
        nonlocal competition
        queue = deque()
        queue.append(node)
        visited[node] = 1
        
        while queue:
            v = queue.popleft()
            for new_v in competition[v]:
                if not visited[new_v]:
                    visited[new_v] = 1
                    queue.append(new_v)
                    competition[node].append(new_v)
                    
    for i in range(1,n+1):
        visited = [0 for _ in range(n+1)]
        bfs(i,visited)
        for node in range(1,n+1):
            competition[node] = list(set(competition[node]))
            
    graph = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for i in range(1,n+1):
        for j in competition[i]:
            graph[i][j] = 1; graph[j][i] = 1
            
    for i in range(1,n+1):
        if sum(graph[i])==n-1:
            answer += 1
            
    return answer