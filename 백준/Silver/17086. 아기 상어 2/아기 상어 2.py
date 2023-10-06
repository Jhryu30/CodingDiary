from collections import deque

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

def dfs(graph, v, visited):
  queue = deque()
  queue.append(v)
  visited[v[0]][v[1]]=1

  while queue:
    x,y = queue.popleft()
    for dx,dy in [[-1,-1], [-1,0], [-1,1], [0,-1], [0,1], [1,-1], [1,0], [1,1]]:
      new_x = x+dx; new_y = y+dy
      if new_x<=-1 or new_y<=-1 or new_x>=N or new_y>=M:
        continue
      elif graph[new_x][new_y]==1:
        return visited[x][y]
      elif not visited[new_x][new_y]:
        visited[new_x][new_y] = visited[x][y]+1
        queue.append([new_x, new_y])
        
result = []
for i in range(N):
  for j in range(M):
    if graph[i][j]==0:
      visited = [[0 for _ in range(M)] for _ in range(N)]
      result.append(dfs(graph, [i,j], visited))

print(max(result))