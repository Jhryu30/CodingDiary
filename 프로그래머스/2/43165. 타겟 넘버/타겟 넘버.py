def solution(numbers, target):
    answer = 0
    N = len(numbers)
    
    def dfs(v=0,val=0):
        nonlocal answer
        if v==N:
            if val==target:
                answer += 1
            return
        
        dfs(v+1,val+numbers[v])
        dfs(v+1,val-numbers[v])
    
    dfs()
    return answer