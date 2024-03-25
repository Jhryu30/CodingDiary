N = int(input())

if not N%2:
  dp = [0 for _ in range(N//2)]
  dp[0] = 3
  for n in range(1,N//2):
    dp[n] =  2*(sum(dp[:n])+1) + dp[n-1]
  print(dp[-1])
else:
  print(0)