from collections import defaultdict
from heapq import heappush, heappop

def solution(n, s, a, b, fares):
    answer = 10**30

    graph = defaultdict(dict)
    for i,j,c in fares:
        graph[i][j] = c
        graph[j][i] = c
        

    def dijkstra(start,goal):
        queue = [(0,start)]
        visited = [10**10 for _ in range(n+1)]
        while queue:
            c,v = heappop(queue)
            if v==goal:
                return c
            for nv in graph[v].keys():
                nc = graph[v][nv]
                if visited[nv]<=c+nc:
                    continue
                visited[nv] = c+nc
                heappush(queue,(c+nc,nv))
    
    for mid in range(1,n+1):
        try:
            mid_cost = dijkstra(s,mid)
            a_cost = dijkstra(mid,a)
            b_cost = dijkstra(mid,b)
            answer = min(answer,mid_cost+a_cost+b_cost)
        except:
            pass

    return answer