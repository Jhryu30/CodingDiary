from collections import defaultdict

def solution(info, edges):
    answer = 0

    graph = defaultdict(list)
    for parent, child in edges:
        graph[parent].append(child)

    def dfs(v, queue, sheep, wolf):
        nonlocal answer, graph
        s, w = (1, 0) if info[v] == 0 else (0, 1)
        sheep += s
        wolf += w
        answer = max(answer, sheep)
        if wolf >= sheep:
            return
        
        for next_v in graph[v]:
            queue.append(next_v)
        for i,new_v in enumerate(queue):
            dfs(new_v, queue[:i]+queue[i+1:], sheep, wolf)

    v = 0
    sheep, wolf = (0, 0)
    dfs(v, [], sheep, wolf)

    return answer