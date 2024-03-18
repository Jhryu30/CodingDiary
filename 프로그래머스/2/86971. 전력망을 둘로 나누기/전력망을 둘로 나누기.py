from collections import defaultdict, deque

def solution(n, wires):
    answer = n
    graph = defaultdict(list)
    for v1,v2 in wires:
        graph[v1].append(v2); graph[v2].append(v1)
        

    def bfs(graph,v,v2,visited):
        queue = deque()
        queue.append(v)
        visited[v] = 1
        cnt = 1
        
        while queue:
            v = queue.popleft()
            for new_v in graph[v]:
                if new_v==v2:
                    continue
                if not visited[new_v]:
                    visited[new_v] = 1
                    cnt += 1
                    queue.append(new_v)
        return cnt
    
        
    for v1,v2 in wires:
        visited = [0 for _ in range(n+1)]
        cnt1 = bfs(graph,v1,v2,visited)
        cnt2 = bfs(graph,v2,v1,visited)
        answer = min(abs(cnt1-cnt2),answer)
    

                    
    return answer