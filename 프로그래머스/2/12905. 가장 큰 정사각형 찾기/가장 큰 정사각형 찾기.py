def solution(board):
    # dp[i][j]: 정사각형의 우측하단이 (i,j)일 때, 해당 정사각형 한 변의 길이 저장
    ans = 0
    M,N = len(board),len(board[0])

    dp = [[0 for _ in range(N)] for _ in range(M)]
    for i in range(M):
        for j in range(N):
            if i==0 or j==0:
                dp[i][j] = board[i][j]
                ans = max(ans,dp[i][j])
                continue
            dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1 if board[i][j] else 0
            ans = max(ans,dp[i][j])

    answer = ans**2

    return answer