N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]

dp = [0 for _ in range(N+1)]

for i in range(N):
  for j in range(i+lst[i][0],N+1):
    dp[j] = max(dp[j], dp[i]+lst[i][1])

print(dp[-1])