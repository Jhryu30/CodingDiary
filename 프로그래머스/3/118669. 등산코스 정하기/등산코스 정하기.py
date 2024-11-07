from heapq import heappush, heappop
from collections import defaultdict

def solution(n, paths, gates, summits):
    answer = []
    summits.sort(reverse=True)
    
    graph = defaultdict(list)
    for i,j,w in paths:
        graph[i].append((j,w))
        graph[j].append((i,w))
    start = defaultdict(int)
    for g in gates:
        start[g] = 1
    
    goal, intensity = n+1, 10000001
    
    def bfs(graph,v):
        nonlocal goal, intensity
        i_, ori_v, queue = 0, v, []
        visited = defaultdict(int)
        for s in summits:
            visited[s] = 1
        for new_v,i in graph[v]:
            if i<=intensity:
                heappush(queue, (i, new_v, i_, visited))
                
        while queue:
            w,v,i_,visited = heappop(queue)
            visited[v] = 1
            i_ = max(w,i_)
            
            if start[v] and i_<=intensity:
                goal, intensity = ori_v, i_
                return
            
            for new_v,i in graph[v]:
                if not visited[new_v] and i<=intensity:
                    heappush(queue,(i, new_v, i_, visited))
    
    
    for v in summits:
        bfs(graph,v)
        
    answer = [goal, intensity]
    
    return answer