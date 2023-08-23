import sys
from collections import deque

R, C = map(int, sys.stdin.readline().split())
graph = [list(sys.stdin.readline()) for _ in range(R)]
visited = [[False for _ in range(C)] for _ in range(R)]

def bfs(graph, v, visited):
  x,y = v
  queue = deque()
  queue.append((x,y))
  visited[x][y] = True

  sheep=0; fox=0
  while queue:
    x,y = queue.popleft()

    for dx,dy in [[-1,0], [1,0], [0,-1], [0,1]]:
      new_x = x+dx; new_y = y+dy

      if new_x<=0 or new_x>=R-1 or new_y<=0 or new_y>=C-1:
        continue

      if not visited[new_x][new_y]:
        visited[new_x][new_y] = True

        if graph[new_x][new_y]=='#':
          continue
        if graph[new_x][new_y]=='v':
          fox += 1
        if graph[new_x][new_y] == 'k':
          sheep += 1
        queue.append((new_x,new_y))

  return sheep, fox

def compare(result):
  sheep, fox = result
  if sheep==0 and fox==0:
    return 0, 0
  elif sheep>fox:
    return sheep, 0
  else:
    return 0, fox

sheep=0; fox=0
for i in range(R):
  for j in range(C):
    s,f = compare(bfs(graph, [i,j], visited))
    sheep+=s; fox+=f
print(sheep, fox)