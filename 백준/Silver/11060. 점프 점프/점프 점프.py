N = int(input())
maze = list(map(int, input().split()))

dp = [1001 for _ in range(N)]
dp[0]=0
for i in range(N):
  for step in range(1,maze[i]+1):
    next_step = i+step
    if next_step>=N:
      continue
    dp[next_step] = min(dp[next_step],dp[i]+1)
    
result = dp[-1] if dp[-1]<1001 else -1
print(result)