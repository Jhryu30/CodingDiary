import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
  u, v = map(int, sys.stdin.readline().split())
  graph[u].append(v); graph[v].append(u)
visited = [False for _ in range(N+1)]

def bfs(graph, v, visited):
  queue = deque()
  queue.append(v)

  while queue:
    v = queue.popleft()
    visited[v] = True
    for new_v in graph[v]:
      if not visited[new_v]:
        visited[new_v] = True
        queue.append(new_v)

cnt = 0
for node in range(1,N+1):
  if not visited[node]:
    bfs(graph, node, visited)
    cnt += 1
print(cnt)