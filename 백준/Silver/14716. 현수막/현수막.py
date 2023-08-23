import sys
from collections import deque
M, N = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
visited = [[False for _ in range(N)] for _ in range(M)]

def dfs(graph, v, visited):
  x,y = v
  queue = deque()
  queue.append((x,y))
  visited[x][y] = True

  while queue:
    x,y = queue.popleft()
    for dx,dy in [[-1,-1],[-1,0],[-1,1], [0,-1],[0,1], [1,-1], [1,0], [1,1]]:
      new_x = x+dx; new_y = y+dy
      if new_x<=-1 or new_x>=M or new_y<=-1 or new_y>=N:
        continue
      if graph[new_x][new_y]==1 and not visited[new_x][new_y]:
        visited[new_x][new_y] = True
        queue.append((new_x, new_y))

cnt = 0
for i in range(M):
  for j in range(N):
    if graph[i][j]==1 and not visited[i][j]:
      dfs(graph, [i,j], visited)
      cnt += 1
print(cnt)