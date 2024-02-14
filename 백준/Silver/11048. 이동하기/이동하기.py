N,M = map(int, input().split())
maze = [list(map(int,input().split())) for _ in range(N)]

dp = [[0 for _ in range(M)] for _ in range(N)]

dp[0][0] = maze[0][0]
for j in range(1,M):
  dp[0][j] = dp[0][j-1]+maze[0][j]
for i in range(1,N):
  dp[i][0] = dp[i-1][0]+maze[i][0]

for j in range(1,M):
  for i in range(1,N):
    dp[i][j] = max(dp[i-1][j],dp[i-1][j-1],dp[i][j-1])+maze[i][j]

print(dp[-1][-1])