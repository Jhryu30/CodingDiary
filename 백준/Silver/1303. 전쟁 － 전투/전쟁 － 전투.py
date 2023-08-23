import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())
graph = [list(sys.stdin.readline()) for _ in range(M)]
visited = [[False for _ in range(N)] for _ in range(M)]

def dfs(graph, v, visited, team_color):
  x,y = v
  queue = deque()
  queue.append((x,y))
  visited[x][y] = True

  team_num = 1
  while queue:
    x,y = queue.popleft()
    for dx, dy in [[-1,0], [1,0], [0,-1], [0,1]]:
      new_x = x+dx; new_y = y+dy
      if new_x<=-1 or new_x>=M or new_y<=-1 or new_y>=N:
        continue
      if graph[new_x][new_y]==team_color and not visited[new_x][new_y]:
        visited[new_x][new_y] = True
        queue.append((new_x, new_y))
        team_num += 1
  return team_num

result = {'B':0, 'W':0}
for i in range(M):
  for j in range(N):
    if not visited[i][j]:
      team_color = graph[i][j]
      result[team_color] += (dfs(graph, [i,j], visited, team_color))**2
print(result['W'], result['B'])