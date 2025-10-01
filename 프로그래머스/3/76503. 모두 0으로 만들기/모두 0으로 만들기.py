from collections import defaultdict, deque

def solution(a, edges):
    answer = 0
    N = len(a)
    
    if not sum(a) == 0:
        return -1

    graph = defaultdict(list)
    degree = [0 for _ in range(N)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
        degree[u] += 1
        degree[v] += 1

    leaves_queue = deque()
    for node in range(N):
        if degree[node] == 1:
            leaves_queue.append(node)

            
    while leaves_queue:
        leaf = leaves_queue.popleft()
        # if degree[leaf] == 0:
        #     continue
            
        parent = -1
        for neighbor in graph[leaf]:
            if degree[neighbor] > 0: 
                parent = neighbor
                break
        
        if parent == -1: 
            break
            
        ans = a[leaf]
        answer += abs(ans)
            
        a[parent] += ans
        a[leaf] = 0
        
        degree[leaf] = 0
        degree[parent] -= 1

        if degree[parent] == 1:
            leaves_queue.append(parent)
    return answer