from collections import defaultdict,deque

def solution(begin, target, words):
    answer = 0
    
    graph = defaultdict(list)
    words.append(begin)
    for i,w1 in enumerate(words[:-1]):
        for j,w2 in enumerate(words[i+1:]):
            cnt = sum([w1[k]!=w2[k] for k in range(len(w1))])
            if cnt==1:
                graph[w1].append(w2)
                graph[w2].append(w1)
                
    def bfs(graph,v,target,visited):
        queue = deque()
        queue.append(v)
        
        while queue:
            v = queue.popleft()
            for new_v in graph[v]:
                if new_v==target:
                    return visited[v]
                
                if not visited[new_v]:
                    visited[new_v] = visited[v]+1
                    queue.append(new_v)
        return 0

    
    visited = {w:0 for w in words}
    visited[begin] = 1
    answer = bfs(graph,begin,target,visited)
    return answer