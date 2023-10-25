def solution(tickets):
    answer = []
    N = len(tickets)
    tickets.sort(key=lambda x:x[1])
    
    def dfs(v,visited,path):
        nonlocal tickets
        if len(path)==N+1:
            # answer.append(path)
            answer.extend(path)
            return 
        
        for i,(dep,arr) in enumerate(tickets):
            if dep == v and not visited[i]:
                visited[i] = 1
                dfs(arr, visited,path+[arr])
                visited[i] = 0
            if len(answer):
                break
    visited = [0 for _ in range(N)]
    dfs('ICN', visited,['ICN'])
    # answer.sort()
    
    # return answer[0]
    return answer