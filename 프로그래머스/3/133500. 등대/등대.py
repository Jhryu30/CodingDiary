from collections import defaultdict

def solution(n, lighthouse):
    answer = 0
    graph = defaultdict(list)
    mydict = defaultdict(list)
    for a,b in lighthouse:
        graph[a].append(b); graph[b].append(a)
        mydict[a].append(b); mydict[b].append(a)
    
    visited = [-1 for _ in range(n+1)]
    # leaf노드부터
    leaves = [node for node in graph.keys() if len(graph[node])==1]
    while n>2:
        n -= len(leaves)
        new_leaves = []
        for leaf in leaves:
            light = 1 if 0 in [visited[new_v] for new_v in mydict[leaf]] else 0
            visited[leaf] = light
            neighbor = graph[leaf].pop()
            graph[neighbor].remove(leaf)
            if len(graph[neighbor])==1:
                new_leaves.append(neighbor)
        leaves = new_leaves
    
    for leaf in leaves:
        light = 1 if 0 in [visited[new_v] for new_v in mydict[leaf]] else 0
        visited[leaf] = light
        
    answer = sum(visited)+1
    return answer