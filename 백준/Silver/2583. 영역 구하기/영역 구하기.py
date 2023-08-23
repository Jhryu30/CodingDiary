import sys
from collections import deque

M, N, K = map(int, sys.stdin.readline().split())
graph = [[1 for _ in range(M)] for _ in range(N)]
for _ in range(K):
  x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
  for x in range(x1,x2):
    graph[x][y1:y2] = [0 for _ in range(y2-y1)]
visited = [[False for _ in range(M)] for _ in range(N)]

def bfs(graph, v, visited):
  x,y = v
  queue = deque()
  queue.append((x,y))
  visited[x][y] = True

  cnt = 1
  while queue:
    x,y = queue.popleft()
    # print(f'{x,y}|{graph[x][y]}|{visited[x][y]}')

    for dx,dy in [[-1,0], [1,0], [0,-1], [0,1]]:
      new_x=x+dx; new_y=y+dy

      if new_x<=-1 or new_x>=N or new_y<=-1 or new_y>=M:
        continue

      if graph[new_x][new_y]==1 and not visited[new_x][new_y]:
        visited[new_x][new_y] = True
        queue.append((new_x, new_y))
        cnt += 1
  
  return cnt

result = []
for x in range(N):
  for y in range(M):
    if graph[x][y]==1 and not visited[x][y]:
      res = bfs(graph, [x,y], visited)
      result.append(res)

print(len(result))
print(*sorted(result))