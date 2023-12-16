def solution(k, dungeons):
    answer = -1
    N = len(dungeons)
    
    def backtracking(k,visited):
        nonlocal answer
        
        if sum(visited)>answer:
            answer = sum(visited)
        
        for v in range(N):
            if not visited[v]:
                need, cost = dungeons[v]
                if k>=need:
                    visited[v] = True
                    backtracking(k-cost,visited)
                    visited[v] = False
                
    visited = [False for _ in range(N)]
    backtracking(k,visited)
    return answer