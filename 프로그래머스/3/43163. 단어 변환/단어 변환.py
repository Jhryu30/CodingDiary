from collections import defaultdict, deque

def solution(begin, target, words):
    answer = 0
    words.append(begin)
    N,n = len(words), len(words[0])
    
    graph = defaultdict(list)
    visited = {k:0 for k in words}
    for i,a in enumerate(words[:-1]):
        for j,b in enumerate(words[i+1:]):
            cnt = sum(a[idx]!=b[idx] for idx in range(n))
            if cnt==1:
                graph[a].append(b); graph[b].append(a)
                
    def bfs(visited):
        nonlocal begin, target, graph
        queue = deque()
        queue.append(begin)
        visited[begin] = 1
        
        while queue:
            v = queue.popleft()
            for new_v in graph[v]:
                if new_v == target:
                    print(v,target)
                    return visited[v]
                if not visited[new_v]:
                    visited[new_v] = visited[v]+1
                    queue.append(new_v)
        return 0
                    
    answer = bfs(visited)
    
    return answer