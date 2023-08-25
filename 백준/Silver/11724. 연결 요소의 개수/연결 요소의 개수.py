import sys
sys.setrecursionlimit(10**5)
N, M = map(int, sys.stdin.readline().rstrip().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
  i,j = map(int, sys.stdin.readline().rstrip().split())
  graph[i].append(j); graph[j].append(i)
visited = [False for _ in range(N+1)]

def dfs(graph, v, visited):
  visited[v] = True
  for new_v in graph[v]:
    if not visited[new_v]:
      dfs(graph, new_v, visited)

cnt = 0
for node in range(1,N+1):
  if not visited[node]:
    dfs(graph, node, visited)
    cnt += 1
print(cnt)