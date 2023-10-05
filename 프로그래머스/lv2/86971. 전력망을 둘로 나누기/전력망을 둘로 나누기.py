from collections import deque

def solution(n, wires):
    answer = -1
    
    def def_graph(wires_lst):
        graph = [[] for _ in range(n+1)]
        
        for w in wires_lst:
            i,j = w
            graph[i].append(j)
            graph[j].append(i)
        for i in range(n+1):
            graph[i].sort()
            
        return graph
    
    cnt = []
    for i in range(len(wires)):
        curr_wires = wires[:i] + wires[i+1:]
        graph = def_graph(curr_wires)
        
        visited = [False for _ in range(n+1)]
        bfs(graph, wires[i][0], visited)
        cnt1 = sum(visited)
        bfs(graph, wires[i][1], visited)
        cnt2 = sum(visited)-cnt1
        
        
        cnt.append(abs(cnt2-cnt1))
        
    answer = min(cnt)
    
    return answer

def bfs(graph, v, visited):
    queue = deque()
    queue.append(v)
    visited[v] = True
    
    while queue:
        v = queue.popleft()
        for new_v in graph[v]:
            if not visited[new_v]:
                visited[new_v] = True
                queue.append(new_v)