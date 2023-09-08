from collections import deque

def solution(begin, target, words):
    answer = 0
    
    if target not in words:
        return answer
    
    words.remove(target)
    words = [begin]+words+[target]
    
    global N
    N = len(words); word_len = len(begin)
    graph = [[] for _ in range(N)]
    for i in range(N):
        for j in range(i,N):
            i_word = words[i]; j_word = words[j]
            if sum([i_word[k]!=j_word[k] for k in range(word_len)])==1:
                graph[i].append(j); graph[j].append(i)
          
    visited = [0 for _ in range(N)]
    answer = bfs(graph, 0, visited)
    return answer


def bfs(graph, v, visited):
    queue = deque()
    queue.append(v)
    visited[v] = 1
    
    while queue:
        v = queue.popleft()
        for new_v in graph[v]:
            if new_v==N-1:
                return visited[v]
            if not visited[new_v]:
                queue.append(new_v)
                visited[new_v] = visited[v]+1
    return 0
                