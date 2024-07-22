def solution(board, skill):
    answer = 0
    
    M,N = len(board[0]), len(board)
    cum_skill = [[0 for _ in range(M+1)] for _ in range(N+1)]
    
    for t,r1,c1,r2,c2,d in skill:
        if t==1:
            d *= -1
            
        cum_skill[r1][c1] += d
        cum_skill[r1][c2+1] -= d
        cum_skill[r2+1][c1] -= d
        cum_skill[r2+1][c2+1] += d
    
    for r in range(N):
        for c in range(1,M):
            cum_skill[r][c] += cum_skill[r][c-1]
    for c in range(M):
        for r in range(1,N):
            cum_skill[r][c] += cum_skill[r-1][c]
    
    for r in range(N):
        for c in range(M):
            if board[r][c]+cum_skill[r][c]>0:
                answer += 1
                
    return answer