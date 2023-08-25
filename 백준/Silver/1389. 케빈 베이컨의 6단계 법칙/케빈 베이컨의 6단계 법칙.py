import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
  i,j = map(int, sys.stdin.readline().split())
  graph[i].append(j); graph[j].append(i)


def bfs(graph, v, visited):
  queue = deque()
  queue.append(v)
  visited[v] = 1

  while queue:
    v = queue.popleft()

    for new_v in graph[v]:
      if not visited[new_v]:
        queue.append(new_v)
        visited[new_v] = visited[v]+1
  
  return sum(visited[1:])-N

result = [0 for _ in range(N+1)]
for node in range(1,N+1):
  visited = [0 for _ in range(N+1)]
  result[node] = bfs(graph, node, visited)

result = result[1:]
print(min(range(len(result)), key=lambda i: result[i])+1)