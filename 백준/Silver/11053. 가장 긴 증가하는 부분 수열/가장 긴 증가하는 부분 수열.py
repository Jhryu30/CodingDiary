N = int(input())
A = list(map(int, input().split())) if N>1 else [int(input())]

dp = [1 for _ in range(N)] # visited처럼

for i in range(N):
  for j in range(i):
    if A[j]<A[i]:
      dp[i] = max(dp[j]+1,dp[i])

print(max(dp))