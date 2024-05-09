def solution(N):
    def n_queen(row, cols, left_diag, right_diag):
        nonlocal answer
        if row == N:
            answer += 1
            return
        
        # 현재 행에 가능한 열 : (N 크기의 열)  & ~(이전에 queen 놓은 열, 왼/오 대각선)
        # 즉, N 크기만큼 가능한 열에서 이전에 놓은 열, 왼/오 대각선에 퀸을 놓은 열은 제외
        available_cols = ((1 << N) - 1) & ~(cols | left_diag | right_diag)
        
        while available_cols:
            pos = available_cols & -available_cols # 가장 오른쪽에 있는 1 찾기
            available_cols -= pos # 찾은 위치에 해당하는 열을 사용하지 않도록 표시 (pos 위치에 0)
            # -> 가능한 열에서 퀸을 배치할 때마다 해당 열을 사용하지 않도록 표시해줌
            
            n_queen(row + 1, cols | pos, (left_diag | pos) << 1, (right_diag | pos) >> 1)
            # cols | pos : pos 열에 퀸 배치
            # (left_diag | pos)<<1 : 왼쪽 대각선 저장에 퀸 배치 체크. 그리고 row+1이니까 얘도 한 칸 옆으로
            
            
    answer = 0
    n_queen(0, 0, 0, 0)
    
    return answer