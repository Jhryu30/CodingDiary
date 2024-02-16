import sys
from collections import defaultdict, deque

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6) 

N = int(input())
pop = [0]+list(map(int, input().split()))
graph = defaultdict(list)
for _ in range(N-1):
  i,j = map(int, input().split())
  graph[i].append(j); graph[j].append(i)
    
def dfs(v, visited, dp):
  global graph
  visited[v] = 1
  
  for new_v in graph[v]:
    if not visited[new_v]:
      dfs(new_v, visited, dp)
      dp[v][0] += dp[new_v][1]
      dp[v][1] += max(dp[new_v])
      
  return dp

visited = [0 for _ in range(N+1)]
dp = [[pop[i],0] for i in range(N+1)] # maximized when [selected[i], not-selected[i]]

dp = dfs(1, visited, dp)
print(max(dp[1]))