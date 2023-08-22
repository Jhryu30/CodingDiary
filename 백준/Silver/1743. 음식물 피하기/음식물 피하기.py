import sys
from collections import deque
N, M, K = map(int, sys.stdin.readline().split())
graph = [[0 for _ in range(M)] for _ in range(N)]
for _ in range(K):
  i,j = map(int, sys.stdin.readline().split())
  graph[i-1][j-1]=1

def bfs(graph, v):
  x,y = v
  queue = deque()
  queue.append((x,y))
  graph[x][y]=0

  cnt = 1
  while queue:
    x,y = queue.popleft()
    for dx,dy in [[-1,0], [1,0], [0,-1], [0,1]]:
      new_x = x + dx
      new_y = y + dy
      if new_x<=-1 or new_x>=N or new_y<=-1 or new_y>=M:
        continue
      if graph[new_x][new_y]==1:
        graph[new_x][new_y] = 0
        queue.append((new_x,new_y))
        cnt += 1
  return cnt

result = []
for i in range(N):
  for j in range(M):
    if graph[i][j]==1:
      result.append(bfs(graph, [i,j]))
print(max(result))