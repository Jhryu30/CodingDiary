def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x:x[2])
    
    visited = [0 for _ in range(n)]
    
    i = costs[0][0]; visited[i] = 1
    
    while sum(visited)<n:
        for i,j,c in costs:
            if visited[i] and visited[j]:
                continue
            if visited[i] or visited[j]:
                visited[i]=1; visited[j]=1
                answer += c
                break
                
    return answer