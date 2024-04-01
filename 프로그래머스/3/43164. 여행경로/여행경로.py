from collections import deque

def solution(tickets):
    N = len(tickets)
    answer = []
    tickets.sort(key=lambda x:x[1])
    
    def dfs(v,route,visited):
        nonlocal tickets
        if len(route)==N+1:
            answer.extend(route)
            return
        
        for i,(dep,arr) in enumerate(tickets):
            if dep==v and not visited[i]:
                visited[i] = 1
                dfs(arr,route+[arr],visited)
                visited[i] = 0
            if len(answer):
                break
                        
    
    visited = [0 for _ in range(len(tickets))]
    dfs(v="ICN",route=["ICN"], visited=visited)
    
    return answer