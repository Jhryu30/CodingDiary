import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]

def bfs(graph, v, visited):
  x,y = v
  queue = deque()
  if graph[x][y]==1:
    queue.append([x,y])
  visited[x][y] = True

  cnt = 1
  while queue:
    x,y = queue.popleft()
    for dx,dy in [[-1,0], [1,0], [0,-1], [0,1]]:
      new_x = x + dx
      new_y = y + dy
      if new_x<=-1 or new_x>=n or new_y<=-1 or new_y>=m:
        continue
      if graph[new_x][new_y]==1 and not visited[new_x][new_y]:
        visited[new_x][new_y] = True
        queue.append([new_x,new_y])
        cnt += 1

  return cnt

result = []
for x in range(n):
  for y in range(m):
    if graph[x][y]==1 and not visited[x][y]:
      result.append(bfs(graph, [x,y], visited))

print(len(result))
if len(result)==0:
  print(0)
else:
  print(max(result))