def dfs(graph, v, visited):
    visited[v] = True
    for new_v in graph[v]:
        if not visited[new_v]:
            dfs(graph, new_v, visited)

def solution(n, computers):
    answer = 0
    
    # 연결된 컴퓨터를 graph로 표현
    graph = [[] for _ in range(n)]
    visited = [False for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if computers[i][j]:
                graph[i].append(j)
    
    # dfs로 연결된 개수 찾기
    for v in range(n):
        if not visited[v]:
            dfs(graph, v, visited)
            answer += 1
            
    return answer