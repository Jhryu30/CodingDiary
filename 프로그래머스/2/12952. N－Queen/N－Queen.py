def solution(N):
    def n_queen(row, cols, left_diag, right_diag):
        nonlocal answer
        if row == N:
            answer += 1
            return
        
        available_cols = ((1 << N) - 1) & ~(cols | left_diag | right_diag)
        
        while available_cols:
            pos = available_cols & -available_cols
            available_cols -= pos
            
            n_queen(row + 1, cols | pos, (left_diag | pos) << 1, (right_diag | pos) >> 1)
            
    answer = 0
    n_queen(0, 0, 0, 0)
    
    return answer